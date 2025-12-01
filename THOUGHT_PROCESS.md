# Thought Process

## When Semantic Similarity Might Fail

Semantic search isn't perfect. "Python" could match snake-related content, "Java" could match the island. Abbreviations like "ML" might embed differently than "Machine Learning". New or niche terms may not work well if the model hasn't seen them enough.

## Mitigation Strategies

Don't rely on semantics alone - combine with other signals. In the demo I use popularity to boost common job titles over obscure ones. For production I'd add keyword matching as fallback when semantic scores are low, and filters by category or seniority. Tracking what users actually click helps the system improve over time and gives it agility to adapt to real usage patterns.