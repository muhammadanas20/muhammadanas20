# Cheatsheet — Phase 4: Docker

Print or pin. This is not a substitute for Theory.md.

## Remember

Service DNS not localhost. COPY reqs first. Non-root. Volumes for data. 0.0.0.0.

## Commands / snippets

```bash
docker compose up --build
docker compose logs -f api
docker compose down -v
docker build -t me/api:0.1 .
docker exec -it NAME bash
```

```python
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Decision tree

Dev deps → compose. Prod single node → compose or PaaS. Multi node → orchestrator.

## Numbers

Slim Python images ~120MB+. Alpine can break manylinux wheels — slim-bookworm is safer.

## Do not

latest in prod. secrets in layers. root. copy .venv. localhost to reach sibling containers.
