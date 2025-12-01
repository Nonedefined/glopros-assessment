# System Design: Job Title & Skill Suggestion Module

## Problem

Build a module that:
1. Suggests **job titles** from free-text input (e.g., "Senior backend engineer with ML interests")
2. Suggests **additional skills** based on selected skills (e.g., ["Python", "Vector Databases"] -> "FastAPI", "LangChain")

---

## High-Level Architecture

```
User Input --> Preprocess --> Embed --> Vector Search --> Rerank --> Response
                  |             |            |              |
               trim          model       Qdrant         combine
                           encode()     top-K         semantic +
                                                      popularity
```

---

## 1. Text Processing

Keep it simple - modern embedding models handle variations well:
- Trim whitespace
- Skip lowercase/stemming/stopwords - model handles semantics better without over-processing

For skill-based queries: concatenate skills into one string `"Python, Vector Databases"` before embedding.

---

## 2. Embeddings & Vector Store

### Embedding Model
**Choice:** `text-embedding-3-small` (OpenAI)
- Good balance of quality and cost
- 1536-dimensional vectors
- Easy to use via API

### Vector Store
**Choice:** Qdrant (in-memory mode for demo, can scale to production)

### Indexing
```python
# Store job titles and skills with metadata
{
    "id": "jt_001",
    "text": "Machine Learning Engineer",
    "vector": [0.02, -0.15, ...],  # 1536 dims
    "metadata": {
        "popularity": 0.85,  # from job market data
        "category": "Engineering"
    }
}
```

---

## 3. Ranking: Semantic + Popularity

Pure semantic search can return obscure matches. Combine with popularity:

```
final_score = 0.7 * semantic_similarity + 0.3 * popularity
```

Weights: semantic is primary signal (0.7), popularity prevents obscure results (0.3). Can be tuned based on user feedback.

- **Semantic similarity** - cosine distance from vector search, captures meaning
- **Popularity** - from job posting frequency or user selections, prevents obscure matches

For skills can also use **co-occurrence** - how often skills appear together in job postings.

---

## 4. Output Structure

### Job Title Suggestions
```json
{
    "query": "Senior backend engineer with ML interests",
    "suggestions": [
        {"title": "Machine Learning Engineer", "score": 0.89},
        {"title": "Senior Software Engineer", "score": 0.84},
        {"title": "Backend Engineer", "score": 0.78}
    ]
}
```

### Skill Suggestions
```json
{
    "query_skills": ["Python", "Vector Databases"],
    "suggestions": [
        {"skill": "LangChain", "score": 0.82},
        {"skill": "FastAPI", "score": 0.76},
        {"skill": "PostgreSQL", "score": 0.71}
    ]
}
```
