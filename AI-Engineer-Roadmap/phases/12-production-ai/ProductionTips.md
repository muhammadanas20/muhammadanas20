# Production tips — Phase 12: Production AI / LLMOps

## Cost

Budgets, routers, caches, smaller models, smaller k. Weekly cost review.

## Latency

TTFT SLO. Cache. Parallel retrieve. Don't chain 5 reflections on the hot path.

## Reliability

Fallback. Timeouts. Queue when overloaded.

## Observability

If you cannot click one user request end-to-end, you are not done.

## Scaling

Stateless API + Redis + PG. Tracer backend sized for span volume.

## The boring checklist

- spans
- eval gate
- budget
- fallback
- redaction
- tenant cache keys

Production is not a later phase. It is a way of writing Tuesday's code.
