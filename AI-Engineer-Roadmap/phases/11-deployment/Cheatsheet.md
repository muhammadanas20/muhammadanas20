# Cheatsheet — Phase 11: Deployment

Print or pin. This is not a substitute for Theory.md.

## Remember

SHA tags. Secrets off git. healthz/readyz. 0.0.0.0. Rollback = old image.

## Commands / snippets

```bash
fly deploy
render/railway dashboards
gh workflow view
```

```python
@app.get("/healthz")\ndef healthz(): return {"ok": True}
```

## Decision tree

One service → PaaS. Many services + team → cloud/k8s later.

## Numbers

Health interval 5–15s. Proxy timeout > model p95. Min 1 instance for chat UX.

## Do not

latest. secrets in images. bind 127.0.0.1. skip smoke.
