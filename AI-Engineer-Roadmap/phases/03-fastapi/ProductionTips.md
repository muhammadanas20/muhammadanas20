# Production tips — Phase 3: FastAPI

## Cost

Auth + rate limits are cost controls. Unauthenticated model endpoints are a credit card on the sidewalk.

## Latency

TTFT (time to first token) is the UX metric. Stream immediately, even a keepalive SSE comment.

## Reliability

Graceful shutdown: stop taking new, finish streams, then kill.

## Observability

Request ID in response header and logs. Later: traces.

## Scaling

Stateless app + Redis + PG. Horizontal scale Uvicorn workers behind a load balancer.

## The boring checklist

- auth
- rate limit
- healthz
- no debug
- timeouts
- tests

Production is not a later phase. It is a way of writing Tuesday's code.
