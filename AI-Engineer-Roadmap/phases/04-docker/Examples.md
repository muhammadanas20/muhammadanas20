# Examples — Phase 4: Docker

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. A cache-friendly Dockerfile

Order of COPY is a performance feature.

```python
# code/Dockerfile
FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home --uid 1000 appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appuser . .
USER appuser
EXPOSE 8000
CMD ["python", "-m", "http.server", "8000"]

```

**What every interesting line is doing**

requirements copied first so code edits reuse the pip layer. USER drops root. EXPOSE is documentation; -p still required.

**Expected output**

```text
docker build -t demo .  then docker run -p 8000:8000 demo
```

**Dry run**

Each instruction commits a layer. Unchanged instructions replay from cache.

**Memory**

Image size = sum of layers (with dedup). Running container adds a thin writable layer.

**Time complexity:** First build minutes; next code-only rebuild seconds if deps unchanged  
**Space complexity:** Image on disk; use docker system df

**Alternatives**

uv in Docker; poetry export to requirements.

**Optimization**

Multi-stage. Combine RUN apt-get with cleanup in the same layer.

---

### Example 2. Compose for API + Postgres + Redis

This is the local production-shaped world.

```python
# code/compose.yaml
services:
  api:
    build: .
    ports: ["8000:8000"]
    environment:
      DATABASE_URL: postgresql://ai:ai@postgres:5432/ai
      REDIS_URL: redis://redis:6379/0
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: ai
      POSTGRES_PASSWORD: ai
      POSTGRES_DB: ai
    volumes: [pgdata:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ai"]
      interval: 5s
      retries: 5
  redis:
    image: redis:7-alpine
volumes:
  pgdata:

```

**What every interesting line is doing**

Hostnames postgres and redis are DNS on the compose network. Volume keeps PG data. Healthcheck stops the API from booting too early.

**Expected output**

```text
docker compose up --build — API logs, PG ready, Redis PONG.
```

**Dry run**

Compose creates network + volume, starts PG/Redis, waits, starts API.

**Memory**

Three processes. PG uses RAM for shared_buffers (default small).

**Time complexity:** Boot in seconds after images exist  
**Space complexity:** pgdata grows with data

**Alternatives**

Tilt, devcontainers, Podman compose.

**Optimization**

profiles for optional services (qdrant). Don't publish PG port on prod machines.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
