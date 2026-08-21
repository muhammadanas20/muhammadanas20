# Exercises — Phase 7: Vector databases

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. Chroma persist

Persist to ./chroma_data, restart process, query still works.

**Constraints:** Not in-memory only.

### B2. Metadata filter

Two tenants. Query with and without filter. Screenshot.

**Constraints:** Show the leak without filter.

## Medium

### M1. pgvector

Store the Phase 6 notes index in PG. Compare top-5 to numpy.

**Constraints:** Overlap table.

### M2. Idempotent upsert

Re-run ingest. Row count stays stable.

**Constraints:** Primary key = chunk hash.

## Hard

### H1. Tradeoff memo

2 pages: Chroma vs pgvector vs Qdrant vs Pinecone for a 5M-chunk SaaS.

**Constraints:** Include cost, ops, filters, lock-in, backup.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase7/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
