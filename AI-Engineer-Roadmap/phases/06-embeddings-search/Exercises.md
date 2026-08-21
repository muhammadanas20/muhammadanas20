# Exercises — Phase 6: Embeddings and search

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. Ten sentences

Embed with a local model (or fake vectors) and print a similarity matrix.

**Constraints:** Same model for all.

### B2. Metadata

Each chunk stores path + heading. Filter search to one file.

**Constraints:** Filter happens before or after kNN — document which.

## Medium

### M1. Token chunker

Chunk by tiktoken counts not chars, overlap 50 tokens.

**Constraints:** No chunk exceeds 400 tokens.

### M2. Eval mini

12 queries with labeled files. Report recall@3.

**Constraints:** Do not tune on the same 12 until you freeze them first.

## Hard

### H1. Hybrid preview

Combine BM25 (or simple TF-IDF) with cosine using a weighted sum. Compare to either alone.

**Constraints:** Table of three systems on the 12 queries.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase6/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
