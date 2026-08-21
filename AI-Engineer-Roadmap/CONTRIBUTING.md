# Contributing

This course is designed to stay current as AI tooling changes.

Models, frameworks, and cloud UIs move fast.
The *engineering principles* move slowly.

Contribute in a way that keeps both true.

## What we want

- Corrections of factual errors
- Clearer explanations (simple English)
- Better diagrams (Mermaid preferred)
- Working code that still runs
- New interview questions with expected answers
- Production war stories (anonymized)
- Translations (keep English as source of truth)
- Links to canonical docs, papers, and official blogs

## What we do not want

- Vendor spam disguised as a lesson
- Uncommented code dumps
- Notebooks that only run on one person's laptop
- Secrets, keys, or proprietary data
- "Just use this paid wrapper" with no first-principles explanation
- Content that skips beginner explanation and jumps to jargon

## How a lesson is structured

Every topic should eventually contain:

1. Introduction
2. Why this exists
3. Real-world analogy
4. Visual diagram
5. Architecture diagram
6. Beginner / intermediate / advanced / production explanations
7. Fully commented code (output, dry run, complexity, alternatives)
8. Exercises (beginner, medium, hard)
9. Project
10. Interview questions
11. Flashcards and quiz
12. Common mistakes and debugging
13. Best practices, industry standards, performance, security
14. References and further reading

If you add a topic, add the supporting files too.
Do not leave `TODO` stubs.

## Code style for examples

- Python 3.11+
- Type hints
- `ruff` clean
- No wildcard imports
- Comments explain *why*, not *what the syntax does* (unless the audience is Phase 0–1)
- Prefer the official SDK over a thin wrapper when teaching a concept
- Show the local / open-source path (Ollama, Chroma, Postgres) before the paid cloud path
- Always include `.env.example`, never `.env`

## Adding a phase or project

1. Open an issue describing the gap.
2. Wait for agreement on scope so we do not duplicate work.
3. Follow the existing folder template in `phases/`.
4. Link the new material from `COURSE_INDEX.md`, `ROADMAP.md`, and the parent `README.md`.
5. Add estimated study time, difficulty, and prerequisites.

## Pull request checklist

- [ ] I read the lesson as a junior engineer would
- [ ] Mermaid diagrams render on GitHub
- [ ] Code examples are complete enough to copy and run
- [ ] I did not commit secrets
- [ ] I updated the index and roadmap if I added a page
- [ ] Interview answers include the *why*, not only the *what*
- [ ] I named tools that may change with a date or version note

## Local preview

Most of this course is Markdown. GitHub rendering is the source of truth.

For Python examples:

```bash
cd AI-Engineer-Roadmap
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Communication

Use GitHub Issues for:

- Broken links
- Outdated APIs
- Requested topics
- Ambiguous explanations

Be kind. Assume good intent. Teach.

Thank you for helping people become AI engineers without a $5,000 invoice.
