import os
import json
import logging
from dotenv import load_dotenv
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from data import (
    EMBEDDING_MODEL, VECTOR_SIZE, JOB_TITLES, SKILLS,
    SEMANTIC_WEIGHT, POPULARITY_WEIGHT, DEFAULT_TOP_K, SEARCH_BUFFER,
)

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

load_dotenv()
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
qdrant = QdrantClient(":memory:")


def get_embeddings(texts: list[str]) -> list[list[float]]:
    response = openai_client.embeddings.create(input=texts, model=EMBEDDING_MODEL)
    return [item.embedding for item in response.data]


def get_embedding(text: str) -> list[float]:
    return get_embeddings([text])[0]


def setup():
    """Create collections and index data."""
    for name, items in [("job_titles", JOB_TITLES), ("skills", SKILLS)]:
        qdrant.create_collection(
            collection_name=name,
            vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
        )
        texts = [item["text"] for item in items]
        embeddings = get_embeddings(texts)
        points = [
            PointStruct(id=i, vector=emb, payload=item)
            for i, (item, emb) in enumerate(zip(items, embeddings))
        ]
        qdrant.upsert(collection_name=name, points=points)


def search(query: str, collection: str, top_k: int = DEFAULT_TOP_K, exclude: list[str] = None):
    """
    Search and rerank results.

    Ranking approach:
    - Get top candidates from vector search (semantic similarity via cosine distance)
    - Rerank using: final_score = 0.7 * semantic + 0.3 * popularity
    - Semantic is primary signal (captures meaning), popularity prevents obscure matches
    """
    exclude = [e.lower() for e in (exclude or [])]
    query_embedding = get_embedding(query.strip())

    results = qdrant.query_points(
        collection_name=collection,
        query=query_embedding,
        limit=top_k + len(exclude) + SEARCH_BUFFER,
    ).points

    ranked = []
    for r in results:
        text = r.payload["text"]
        if text.lower() in exclude:
            continue
        final_score = SEMANTIC_WEIGHT * r.score + POPULARITY_WEIGHT * r.payload["popularity"]
        ranked.append({"text": text, "score": round(final_score, 3)})

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked[:top_k]


def suggest_job_titles(description: str, top_k: int = DEFAULT_TOP_K) -> dict:
    results = search(description, "job_titles", top_k)
    return {
        "query": description,
        "suggestions": [{"title": r["text"], "score": r["score"]} for r in results]
    }


def suggest_skills(selected_skills: list[str], top_k: int = DEFAULT_TOP_K) -> dict:
    query = ", ".join(selected_skills)
    results = search(query, "skills", top_k, exclude=selected_skills)
    return {
        "query_skills": selected_skills,
        "suggestions": [{"skill": r["text"], "score": r["score"]} for r in results]
    }


def main():
    logger.info("Setting up...")
    setup()

    query = "Senior backend engineer with ML interests"
    result = suggest_job_titles(query)
    logger.info("---Job Title Suggestions---")
    logger.info(json.dumps(result, indent=2))

    selected = ["Python", "Vector Databases"]
    result = suggest_skills(selected)
    logger.info("---Skill Suggestions---")
    logger.info(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()