# Exercises — Phase 8: Retrieval-Augmented Generation (RAG)

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. Naive over notes

Index NOTES or this phase folder. 8 questions.

**Constraints:** Print retrieved chunks before the answer.

### B2. I don't know

Add 4 adversarial questions. All must refuse.

**Constraints:** No extra facts from world knowledge.

## Medium

### M1. Hybrid + RRF

BM25 + dense. Table vs dense-only recall@5.

**Constraints:** Same gold set.

### M2. Rerank

Take k=20, rerank to 5 (cross-encoder or a cheap LLM score). Latency vs quality.

**Constraints:** Record p95.

## Hard

### H1. Parent retrieval

Small child chunks for search, parent section for the prompt.

**Constraints:** Diagram + eval.

### H2. Mini CRAG

Grade context; if bad, retry with rewrite. Cost multiplier reported.

**Constraints:** Must not infinite loop.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase8/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
