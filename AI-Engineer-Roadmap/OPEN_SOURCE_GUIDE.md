# Open source guide

You do not need a company logo to prove you can engineer.

A thoughtful pull request on a real project beats 12 unfinished course clones.

---

## Why this matters for AI jobs

AI libraries move fast. Maintainers need:

- Reproducible bug reports
- Eval sets
- Docs that a junior can follow
- Type hints
- Small features with tests

That is the same muscle as the job.

---

## Where to contribute (good first)

Start with tools you **already use in this course**:

- FastAPI / Pydantic / SQLAlchemy / Typer
- Chroma, Qdrant clients
- Ragas, DeepEval, Promptfoo
- LangGraph examples
- MCP servers / SDKs
- Ollama docs and model cards
- This repository (see [CONTRIBUTING.md](./CONTRIBUTING.md))

Search: `label:good-first-issue` plus a language you know.

Avoid: drive-by README badge PRs. Maintainers hate them. Hiring managers ignore them.

---

## A first PR that looks senior

1. Use the project for a week
2. Hit a sharp edge (unclear error, missing example)
3. Open an issue with: what you did, what you expected, what happened, versions
4. Wait. Do not dump a 2,000-line refactor
5. PR: smallest change, test, screenshot if docs

Template:

```
Fixes #123

## Change
Add a timeout example to the RAG client docs.

## Test
Ran `pytest tests/test_client.py -q`
```

---

## Building in public without being annoying

Weekly:

- One commit on your capstone
- One short write-up (even in `NOTES/`)
- One conversation with a human

Do not auto-post "day 47 of 100" with a ChatGPT screenshot.

---

## License hygiene

When you copy code from this course into your portfolio:

- This course is MIT. Keep the license notice if you copy substantial files.
- Do not copy someone else's dataset if the license forbids it.
- Do not upload internal company docs to a public RAG demo. Ever.

---

## MCP / model cards / evals as contribution

High-value, still rare:

- A tiny eval set for a domain (with license)
- An MCP server for a tool you actually use
- A reproduction of a paper's RAG number on a public corpus
- A failed experiment write-up ("hybrid search did nothing on this corpus because…")

Failed experiments with numbers are gold. The industry is drowning in successful-looking screenshots.
