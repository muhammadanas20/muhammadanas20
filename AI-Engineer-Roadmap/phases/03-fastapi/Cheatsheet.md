# Cheatsheet — Phase 3: FastAPI

Print or pin. This is not a substitute for Theory.md.

## Remember

POST chat. JWT in header. SSE for tokens. Depends for auth. No debug in prod.

## Commands / snippets

```bash
uvicorn app.main:app --reload --port 8000
http :8000/docs
```

```python
return StreamingResponse(gen(), media_type='text/event-stream')
```

## Decision tree

One-way stream → SSE. Bidirectional → WS. Heavy job → queue not BackgroundTasks.

## Numbers

JWT access 15–30 min. Workers ≈ cores. Body limits: set them.

## Do not

Secrets in query. CORS *. 200 on errors. Blocking I/O in async.
