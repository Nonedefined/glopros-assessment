# Job Title & Skill Suggestions

Demo module that suggests job titles from text input and related skills based on selected skills.

## Setup

```
pip install -r requirements.txt
```

Create `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_key_here
```

## Run

```
python demo.py
```

## How it works

- Uses OpenAI embeddings (text-embedding-3-small) for semantic similarity
- Stores vectors in Qdrant (in-memory)
- Combines semantic score with popularity for ranking

## Files

- `demo.py` - main code
- `data.py` - constants and sample data
- `SYSTEM_DESIGN.md` - architecture overview
- `THOUGHT_PROCESS.md` - limitations and mitigations
- `bonus/` - analysis of existing solution (GloPros)