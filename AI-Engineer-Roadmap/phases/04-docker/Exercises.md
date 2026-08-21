# Exercises — Phase 4: Docker

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. .dockerignore

Prove .venv is not in the image (docker history / dive / du).

**Constraints:** Before and after screenshot or CLI output.

### B2. Port map

Map 8080:8000. Explain the two numbers.

**Constraints:** One paragraph.

## Medium

### M1. Healthcheck

API healthcheck curls /healthz. Compose restart on failure.

**Constraints:** Show docker ps healthy.

### M2. Dev bind mount

Live-reload uvicorn with a bind mount without copying .venv from host.

**Constraints:** Document the Darwin vs Linux venv issue.

## Hard

### H1. Multi-stage + non-root + scan

Final image < 200MB. Trivy or docker scout notes. Fix HIGH if easy.

**Constraints:** Write what you ignored and why.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase4/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
