# Production tips — Phase 1: Python refresh

## Cost

Retries multiply cost. Cap them. Do not retry 400s from a bad prompt.

## Latency

First-byte latency matters more than total time for chat UX. Stream.

## Reliability

Timeouts + bounded retries + jitter. Measure retry rate.

## Observability

Log attempt number and latency. Later: traces.

## Scaling

One AsyncClient (connection pool) per process, not per request.

## The boring checklist

- timeouts
- retries capped
- pydantic on inputs and LLM outputs
- no time.sleep in async

Production is not a later phase. It is a way of writing Tuesday's code.
