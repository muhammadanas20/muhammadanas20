# RAG cheatsheet

```
ingest: load → chunk → embed → store + metadata
query:  rewrite? → hybrid retrieve → filter → rerank → prompt → generate → cite
eval:   freeze gold → recall@k → faithfulness → CI gate
```

- Same embedding model in and out
- Structure-aware chunks; don't slice tables
- Hybrid (BM25 + dense) + RRF, then rerank 20→5
- k bigger is not always better (lost in the middle)
- Citations ⊆ retrieved ids
- "I don't know" is a feature
- Tenant filter on every query
- GraphRAG is usually later, not first
