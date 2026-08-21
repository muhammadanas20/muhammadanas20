# Cheatsheet — Phase 7: Vector databases

Print or pin. This is not a substitute for Theory.md.

## Remember

Rebuildable index. Match dim + metric. Filter tenant. Don't expose. pgvector is a valid start.

## Commands / snippets

```bash
docker compose up qdrant postgres
# chroma persist dir ./chroma_data
```

```python
col.query(query_embeddings=[q], n_results=5, where={'tenant': tid})
```

## Decision tree

< few million + have PG → pgvector. Need fancy filters/scale → Qdrant. No ops team → managed.

## Numbers

HNSW RAM often 1.5–3× raw vectors. p95 search tens of ms typical.

## Do not

Internet-exposed DB. Metric mismatch. Vectors without text. Forget tenant filter.
