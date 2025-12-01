EMBEDDING_MODEL = "text-embedding-3-small"
VECTOR_SIZE = 1536

# Ranking weights
SEMANTIC_WEIGHT = 0.7
POPULARITY_WEIGHT = 0.3

# Search settings
DEFAULT_TOP_K = 5
SEARCH_BUFFER = 5  # extra results to fetch for reranking

# Job titles with popularity scores (0.0 - 1.0)
JOB_TITLES = [
    {"text": "Software Engineer", "popularity": 0.95},
    {"text": "Senior Software Engineer", "popularity": 0.90},
    {"text": "Backend Engineer", "popularity": 0.85},
    {"text": "Frontend Engineer", "popularity": 0.80},
    {"text": "Full Stack Developer", "popularity": 0.82},
    {"text": "Machine Learning Engineer", "popularity": 0.78},
    {"text": "Data Scientist", "popularity": 0.75},
    {"text": "Data Engineer", "popularity": 0.72},
    {"text": "DevOps Engineer", "popularity": 0.70},
    {"text": "Site Reliability Engineer", "popularity": 0.65},
    {"text": "AI Engineer", "popularity": 0.68},
    {"text": "Python Developer", "popularity": 0.74},
    {"text": "Cloud Architect", "popularity": 0.60},
    {"text": "Tech Lead", "popularity": 0.55},
    {"text": "Engineering Manager", "popularity": 0.50},
]

# Skills with popularity scores
SKILLS = [
    {"text": "Python", "popularity": 0.95},
    {"text": "JavaScript", "popularity": 0.92},
    {"text": "TypeScript", "popularity": 0.85},
    {"text": "SQL", "popularity": 0.88},
    {"text": "PostgreSQL", "popularity": 0.75},
    {"text": "MongoDB", "popularity": 0.70},
    {"text": "Redis", "popularity": 0.65},
    {"text": "Docker", "popularity": 0.80},
    {"text": "Kubernetes", "popularity": 0.68},
    {"text": "AWS", "popularity": 0.82},
    {"text": "Machine Learning", "popularity": 0.72},
    {"text": "Deep Learning", "popularity": 0.60},
    {"text": "PyTorch", "popularity": 0.58},
    {"text": "TensorFlow", "popularity": 0.55},
    {"text": "LangChain", "popularity": 0.50},
    {"text": "Vector Databases", "popularity": 0.45},
    {"text": "FastAPI", "popularity": 0.62},
    {"text": "Django", "popularity": 0.68},
    {"text": "React", "popularity": 0.78},
    {"text": "Node.js", "popularity": 0.75},
    {"text": "Git", "popularity": 0.90},
    {"text": "REST APIs", "popularity": 0.85},
    {"text": "GraphQL", "popularity": 0.55},
    {"text": "CI/CD", "popularity": 0.70},
]