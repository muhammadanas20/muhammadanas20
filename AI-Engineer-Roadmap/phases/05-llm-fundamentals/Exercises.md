# Exercises — Phase 5: LLM fundamentals

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. Prompt file

Move a prompt to prompts/classify_v1.txt and load it in code. Change to v2 without editing Python logic.

**Constraints:** Git diff shows the prompt, not a 200-line py.

### B2. max_tokens

Summarize a paragraph with max_tokens=16. Observe truncation. Handle it.

**Constraints:** Detect finish_reason.

## Medium

### M1. Resume extractor

Pydantic Resume model. Parse a messy text resume.

**Constraints:** Retry once with error message in the prompt.

### M2. Cost estimator

Function that given model prices and token counts returns USD. Table for 1k requests.

**Constraints:** Prices in a config file, not hardcoded in three places.

## Hard

### H1. Real tool loop

Against Ollama or OpenAI: model may call `add(a,b)` or `now()`. Max 4 steps. Stream final.

**Constraints:** Unknown tools return an error object, not an exception crash.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase5/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
