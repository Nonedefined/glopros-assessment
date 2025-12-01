# GloPros Suggestions Analysis

Tested autocomplete suggestions on glopros.com

## Job Titles

**Machine Learning Engineer** - suggests "Learning & Development Support Consultant". Looks like keyword match on "Learning" instead of understanding the meaning.

**DevOps** - suggests DevOps Lead, DevOps Analyst, but also "Sports Information Director" which makes no sense.

**Frontend Developer** and **Full Stack** - suggestions are reasonable (Web Developer, Software Engineer, etc).

## Skills

**Python** - suggests Data Science, Go, Bash, Perl. Missing popular stuff like Django, FastAPI.

**React** - suggests ECMAScript versions, Browserify, Enzyme. Enzyme is deprecated, Browserify rarely used now.

**AWS** - suggestions are fine (Cloud Infrastructure, EC2, etc).

**Docker, Kubernetes** - no suggestions at all.

## What could be improved

- Tune search to prioritize meaning over keyword overlap
- Update skill database with modern tools
- Add popularity weighting so common titles/skills rank higher
- Handle multiple skills in one query