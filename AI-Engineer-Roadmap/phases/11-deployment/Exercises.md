# Exercises — Phase 11: Deployment

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. healthz

Add both endpoints. curl them.

**Constraints:** readyz fails if you set a fake flag.

### B2. Dockerfile CMD

0.0.0.0 in prod image.

**Constraints:** Prove 127.0.0.1 is unreachable from host map.

## Medium

### M1. GHCR

Build and push an image tagged with SHA.

**Constraints:** Public or private with a note.

### M2. Release command

Run a dummy migration before start.

**Constraints:** Document order.

## Hard

### H1. Full pipeline

test → build → deploy → smoke.

**Constraints:** README rollback.

### H2. Nginx SSE

Local nginx in front of uvicorn; fix buffering.

**Constraints:** curl -N shows chunks.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase11/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
