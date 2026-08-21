# FastAPI + Docker cheatsheet

- POST for chat; JWT in Authorization
- SSE: `text/event-stream` + `X-Accel-Buffering: no`
- Depends() for auth
- `/healthz` live, `/readyz` deps
- Bind **0.0.0.0**
- COPY requirements before COPY code
- Non-root user
- Compose DNS: `postgres` not localhost
- Tag images with git SHA, not latest
- Secrets in the platform, not Git
