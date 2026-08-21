# Production tips — Phase 4: Docker

## Cost

Image size is pull time which is deploy time which is money on CI minutes.

## Latency

Cold start = pull + boot. Smaller + fewer layers + min deps.

## Reliability

Healthchecks, restart: unless-stopped, pin tags.

## Observability

Logs to stdout. docker compose logs. Later: ship to a backend.

## Scaling

Compose scales poorly across machines. That's when Fly/ECS/K8s appear.

## The boring checklist

- dockerignore
- non-root
- pin tags
- health
- no secrets in image
- 0.0.0.0

Production is not a later phase. It is a way of writing Tuesday's code.
