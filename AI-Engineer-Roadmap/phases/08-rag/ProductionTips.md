# Production tips — Phase 8: Retrieval-Augmented Generation (RAG)

## Cost

Rerankers and agentic loops multiply spend. Cache retrieval for identical questions. Smaller generate model if grounded.

## Latency

Parallel BM25+dense. Stream tokens. Don't GraphRAG on the hot path.

## Reliability

Index freshness. Rebuild. Version. Empty retrieval → abstain, not improv.

## Observability

Trace retrieved ids, scores, prompt version, faithfulness sample.

## Scaling

The retrieve path scales with the vector DB. The generate path scales with the provider. Separate SLOs.

## The boring checklist

- gold set
- abstain
- citations checked
- tenant filter
- hybrid or evidence it is unnecessary
- CI eval

Production is not a later phase. It is a way of writing Tuesday's code.
