# Production tips — Phase 11: Deployment

## Cost

Scale to zero vs min 1. Token spend still dwarfs a $7 VM. Watch both.

## Latency

Region, cold start, proxy. Measure from the user's geography if you can.

## Reliability

Health, retries at the edge, multi-AZ when money exists.

## Observability

Stdout logs now. Traces next phase.

## Scaling

Horizontal replicas of stateless API. State in PG/Redis.

## The boring checklist

- HTTPS
- secrets
- SHA tag
- health
- smoke
- rollback

Production is not a later phase. It is a way of writing Tuesday's code.
