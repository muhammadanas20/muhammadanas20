# Production tips — Phase 6: Embeddings and search

## Cost

Embedding is cheap vs chat. Still cache and skip unchanged hashes. Don't re-embed the world every deploy.

## Latency

Brute force to ~100k is often <50ms. Then ANN. Batch queries.

## Reliability

Idempotent indexer. Checksums. Model id in the index header.

## Observability

Log query, top-k ids, scores. Later: retrieval traces.

## Scaling

Phase 7. Don't build a distributed ANN on day one.

## The boring checklist

- same model
- metadata
- eval@k
- hashes
- no secrets embedded

Production is not a later phase. It is a way of writing Tuesday's code.
