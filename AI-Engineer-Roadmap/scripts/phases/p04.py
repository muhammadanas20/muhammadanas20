PHASE = {
    "num": "4",
    "title": "Docker",
    "tagline": "If it only runs on your laptop, it does not run.",
    "hours": "5-7 days",
    "difficulty": "Medium",
    "exit_ticket": "`docker compose up` runs the Phase 3 API with Postgres and Redis.",
    "objectives": [
        "Write a Dockerfile with a non-root user and a slim base image.",
        "Explain layers, cache, and why COPY order matters.",
        "Use Compose for app + Postgres + Redis.",
        "Mount volumes and attach networks on purpose.",
        "Add healthchecks and a .dockerignore.",
    ],
    "prerequisites": ["Phase 0 Docker installed. Phase 3 app exists or use the stub in code/."],
    "topics": ["Images", "layers", "Compose", "volumes", "networks", "healthchecks", "multi-stage"],
    "nav": "[Home](../../README.md) · Prev: [Phase 3](../03-fastapi/) · Next: [Phase 5 · LLMs](../05-llm-fundamentals/)",
    "theory": {
        "intro": """Docker packages an application with the OS bits it needs into an **image**. A running image is a **container**.

You will use it to:

- Run Postgres without installing it on your laptop
- Make CI match production
- Ship the API in Phase 11

Docker is not Kubernetes. Learn boxes before clusters.""",
        "one_liner": "A container is a process with a boxed-in filesystem and network.",
        "why": """Python versions, system libraries (`libpq`), and 'it works on Apple Silicon' bugs vanish when everyone runs the same image.

AI stacks add extra pain: tokenizers with native wheels, Postgres, Redis, sometimes a vector DB. Compose is how a junior looks senior on day one of a take-home.""",
        "if_missing": "your README would say 'install these 11 things' and nobody would.",
        "analogy": """Lunch boxes.

- **Image** = a packed lunch recipe frozen in time (immutable).
- **Container** = one lunch box made from that recipe, eaten at a table (running process).
- **Layer** = each instruction (FROM, RUN, COPY) is a slice of the sandwich. Unchanged slices are reused (cache).
- **Volume** = a fridge shelf that survives throwing the box away (database files).
- **Network** = the office kitchen: containers can find each other by name (`postgres:5432`).
- **Compose** = a picnic plan: who brings what, which table, which cooler.""",
        "visual": """```mermaid
flowchart TB
  DF[Dockerfile] --> IMG[Image layers]
  IMG --> CTR[Container process]
  CTR --> VOL[(Volume: pgdata)]
  CTR --> NET[Bridge network]
  CMP[compose.yaml] --> CTR
  CMP --> PG[postgres container]
  CMP --> RD[redis container]
```""",
        "architecture": """```mermaid
flowchart LR
  Host[localhost:8000] --> API[api:8000]
  API --> PG[postgres:5432]
  API --> RD[redis:6379]
  PG --> VOL[(pgdata volume)]
```""",
        "beginner": """**Dockerfile** = recipe. `FROM python:3.12-slim` starts from a small Python image.

**Build** = `docker build -t myapi .` creates an image.

**Run** = `docker run -p 8000:8000 myapi` starts a container. `-p host:container` publishes a port.

**.dockerignore** = like .gitignore for the build context. Always ignore `.venv` and `.git` or your image will be huge and slow.

**Compose** = YAML listing services, networks, volumes. `docker compose up --build`.

**Volume** = named persistent disk. Databases need one or `docker compose down -v` will wipe data.

**Healthcheck** = a command Docker runs to see if the process is actually ready (not just started).""",
        "intermediate": """**Layer caching.** Put `COPY requirements.txt` and `RUN pip install` *before* `COPY . .` so code changes do not reinstall deps.

**Multi-stage builds.** Compile in a fat image, copy artifacts to a slim runtime image.

**User.** Don't run as root. `useradd -m app && USER app`.

**Bind mount vs volume.** Bind (`.:/app`) is for live dev (careful with .venv). Named volume is for data.

**Networks.** Compose creates a network; service names are DNS. The API connects to `postgres` not `localhost`. Inside a container, localhost is *itself*.

**Env files.** `env_file: .env` — still don't commit secrets. Compose can pass them.""",
        "advanced": """**BuildKit cache mounts** for pip.

**Distroless / scratch** images for Go; for Python, slim is enough. Distroless debugging is painful.

**Read-only root filesystem** + tmpfs.

**seccomp, drop capabilities.** Default is already better than a VM full of extras.

**Multi-arch.** `buildx` for amd64+arm64.

**Init.** `init: true` so zombies get reaped.

**tmpfs** for sensitive temp files.""",
        "production": """Pin image digests or at least tags (`python:3.12.6-slim` not `:latest`). Scan images (Trivy). Non-root. Resource limits (`mem_limit`). Healthchecks + restart policies. Logs to stdout. Secrets via the platform, not baked in layers (layers keep history — a deleted secret in a later layer is still in the image).

Kubernetes later: a Pod is a wrapper around one or more containers. If you cannot write a Dockerfile you cannot debug a Pod.""",
        "when": "Any service with dependencies. Any deploy. Any CI.",
        "when_not": "A 10-line script. Don't containerize your text editor. Don't start with K8s.",
        "code_preview": '''# Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER nobody
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
''',
        "code_notes": "`0.0.0.0` is required — binding 127.0.0.1 inside the container is unreachable from the host. `--no-cache-dir` keeps the image smaller.",
        "ex_b": "Dockerize a hello FastAPI. curl localhost:8000/healthz.",
        "ex_m": "Compose with Postgres. App waits for healthy PG.",
        "ex_h": "Multi-stage slim image under 200MB. Non-root. Trivy scan notes.",
        "project": "Full stack compose — MiniProject.md.",
        "interview_preview": "Image vs container. Why COPY order. localhost inside a container. Volume vs bind.",
        "flash_sample": "**Q:** Why 0.0.0.0?\n**A:** Listen on all interfaces inside the container so port mapping works.",
        "mistakes_preview": "COPY . then pip install (broken cache). Running as root. Bind-mounting over /app and hiding installed packages. Using latest.",
        "debug_preview": "Cannot connect to postgres@localhost from the API container. Image huge because .venv copied. Permission denied as non-root on a volume.",
        "best": "Pin tags. .dockerignore. Non-root. Healthchecks. One process per container. Logs stdout.",
        "industry": "Compose for dev. Cloud Run / Fly / ECS / K8s for prod. GitHub Actions builds and pushes images.",
        "perf": "Small images pull faster. Layer cache in CI (actions/cache or registry cache). Don't apt-get upgrade blindly.",
        "security": "No secrets in ENV in the Dockerfile. Scan. Non-root. Don't expose Docker socket to random containers.",
        "refs": "- [Docker docs](https://docs.docker.com/)\n- [Compose spec](https://docs.docker.com/compose/compose-file/)",
        "further": "[100 Days of Docker](https://github.com/DARKANGEL689/100-Days-Of-Docker)",
    },
    "examples": [
        {
            "title": "A cache-friendly Dockerfile",
            "why": "Order of COPY is a performance feature.",
            "code": '''# code/Dockerfile
FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home --uid 1000 appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appuser . .
USER appuser
EXPOSE 8000
CMD ["python", "-m", "http.server", "8000"]
''',
            "line_by_line": "requirements copied first so code edits reuse the pip layer. USER drops root. EXPOSE is documentation; -p still required.",
            "output": "docker build -t demo .  then docker run -p 8000:8000 demo",
            "dry_run": "Each instruction commits a layer. Unchanged instructions replay from cache.",
            "memory": "Image size = sum of layers (with dedup). Running container adds a thin writable layer.",
            "time": "First build minutes; next code-only rebuild seconds if deps unchanged",
            "space": "Image on disk; use docker system df",
            "alternatives": "uv in Docker; poetry export to requirements.",
            "optimization": "Multi-stage. Combine RUN apt-get with cleanup in the same layer.",
        },
        {
            "title": "Compose for API + Postgres + Redis",
            "why": "This is the local production-shaped world.",
            "code": '''# code/compose.yaml
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
''',
            "line_by_line": "Hostnames postgres and redis are DNS on the compose network. Volume keeps PG data. Healthcheck stops the API from booting too early.",
            "output": "docker compose up --build — API logs, PG ready, Redis PONG.",
            "dry_run": "Compose creates network + volume, starts PG/Redis, waits, starts API.",
            "memory": "Three processes. PG uses RAM for shared_buffers (default small).",
            "time": "Boot in seconds after images exist",
            "space": "pgdata grows with data",
            "alternatives": "Tilt, devcontainers, Podman compose.",
            "optimization": "profiles for optional services (qdrant). Don't publish PG port on prod machines.",
        },
    ],
    "practice": [
        {"title": "Build and run", "body": "Build the example image. Exec into it. cat /etc/os-release. Observe you are in Debian-slim, not your Mac.", "done": "You felt the isolation."},
        {"title": "Break the cache on purpose", "body": "Change a line of Python vs requirements.txt. See which rebuilds.", "done": "You can predict cache hits."},
        {"title": "down -v", "body": "Write data to PG, compose down, up, data still there. Then down -v, data gone.", "done": "You respect volumes."},
    ],
    "exercises": {
        "beginner": [
            {"title": ".dockerignore", "body": "Prove .venv is not in the image (docker history / dive / du).", "constraints": "Before and after screenshot or CLI output."},
            {"title": "Port map", "body": "Map 8080:8000. Explain the two numbers.", "constraints": "One paragraph."},
        ],
        "medium": [
            {"title": "Healthcheck", "body": "API healthcheck curls /healthz. Compose restart on failure.", "constraints": "Show docker ps healthy."},
            {"title": "Dev bind mount", "body": "Live-reload uvicorn with a bind mount without copying .venv from host.", "constraints": "Document the Darwin vs Linux venv issue."},
        ],
        "hard": [
            {"title": "Multi-stage + non-root + scan", "body": "Final image < 200MB. Trivy or docker scout notes. Fix HIGH if easy.", "constraints": "Write what you ignored and why."},
        ],
    },
    "assignments": [
        {
            "title": "Compose the chat API",
            "time": "3–5 hours",
            "brief": "Dockerize Phase 3 stub + Postgres + Redis. README with three commands. Healthchecks green.",
            "deliverables": ["Dockerfile", "compose.yaml", ".dockerignore", "README"],
            "rubric": ["non-root", "cached layers", "volume for PG", "no secrets in image"],
        }
    ],
    "quiz": [
        {"q": "An image is:", "choices": {"A": "A running process", "B": "An immutable snapshot/recipe result", "C": "A volume", "D": "A JWT"}, "answer": "B", "explain": "Container is the running instance."},
        {"q": "localhost inside a container is:", "choices": {"A": "The host machine", "B": "That container", "C": "Docker Hub", "D": "Postgres always"}, "answer": "B", "explain": "Use service names."},
        {"q": "COPY reqs then pip then COPY code:", "choices": {"A": "Stupid", "B": "Enables layer cache for deps", "C": "Required by Python", "D": "Insecure"}, "answer": "B", "explain": "Cache."},
        {"q": "Named volumes are for:", "choices": {"A": "Source code usually", "B": "Persistent data like PG", "C": "JWTs", "D": "DNS"}, "answer": "B", "explain": "Data."},
        {"q": "0.0.0.0 means:", "choices": {"A": "Listen on all interfaces", "B": "Disable network", "C": "IPv6 only", "D": "Localhost only"}, "answer": "A", "explain": "Needed in containers."},
        {"q": "compose down -v:", "choices": {"A": "Removes volumes too", "B": "Updates Python", "C": "Pushes images", "D": "Is a no-op"}, "answer": "A", "explain": "Data loss if you needed it."},
        {"q": "Running as root in a container:", "choices": {"A": "Best practice", "B": "Increases blast radius if escaped", "C": "Required for Python", "D": "Faster"}, "answer": "B", "explain": "Drop privileges."},
        {"q": ".dockerignore should include:", "choices": {"A": ".venv and .git", "B": "Only .py files", "C": "Dockerfile", "D": "requirements.txt"}, "answer": "A", "explain": "Keep context small."},
        {"q": "Healthcheck vs started:", "choices": {"A": "Same", "B": "Healthy means the app is ready, not just the process spawned", "C": "Healthcheck is for images only", "D": "Compose cannot wait"}, "answer": "B", "explain": "depends_on condition."},
        {"q": ":latest tag in prod:", "choices": {"A": "Recommended", "B": "Not reproducible", "C": "A security feature", "D": "Faster deploys always"}, "answer": "B", "explain": "Pin versions."},
    ],
    "flashcards": [
        {"q": "Image vs container?", "a": "Image = snapshot. Container = running instance."},
        {"q": "Why slim?", "a": "Smaller, fewer packages, smaller attack surface."},
        {"q": "DNS name of a compose service?", "a": "The service key, e.g. postgres."},
        {"q": "What does -p 8000:8000 mean?", "a": "Host 8000 → container 8000."},
        {"q": "Why not copy .venv?", "a": "Wrong OS/arch; huge; shadows image packages."},
        {"q": "Bind mount use?", "a": "Live code in dev."},
        {"q": "Multi-stage?", "a": "Build in one image, copy artifacts to a small runtime image."},
        {"q": "Where do logs go?", "a": "Stdout/stderr so the platform collects them."},
        {"q": "Secret in Dockerfile ENV?", "a": "Lives in image history. Don't."},
        {"q": "init: true?", "a": "Reap zombie processes."},
    ],
    "interview": [
        {
            "q": "Walk me through a good Python Dockerfile.",
            "junior": "Slim base, workdir, copy requirements, pip, copy app, non-root, CMD uvicorn 0.0.0.0, dockerignore.",
            "mistakes": "FROM python:latest, run as root, pip as a separate surprise every build.",
            "senior": "Multi-stage, hash pins, SBOM, distroless tradeoffs, BuildKit caches, non-root + writable /tmp.",
        },
        {
            "q": "App cannot reach Postgres in Compose.",
            "junior": "They're using localhost. Should use hostname postgres. Also wait for healthy.",
            "mistakes": "Reinstall Docker as first step.",
            "senior": "Networks, multiple compose files, IPv6, pg_hba, password env mismatch.",
        },
        {
            "q": "Image vs VM?",
            "junior": "Containers share the host kernel; VMs virtualize hardware. Containers start faster and are denser.",
            "mistakes": "Containers are 'just VMs'.",
            "senior": "Isolation limits, noisy neighbor, Windows containers vs Linux, when VMs still win (hostile multi-tenant).",
        },
        {
            "q": "How do you keep images small?",
            "junior": "Slim base, no-cache pip, dockerignore, multi-stage, combine RUN, no extra apt.",
            "mistakes": "Delete files in a later layer and expect size to drop fully (whiteout still costs unless squashed).",
            "senior": "dive to inspect layers, distroless, compressing wheels, not baking models into images.",
        },
        {
            "q": "Is Compose production-ready?",
            "junior": "Great for single-node and small deploys. For multi-node, use a scheduler (Fly, ECS, K8s).",
            "mistakes": "Compose is only for demos / Compose is enough for Netflix.",
            "senior": "Compose in CI, Swarm (rare), kube compose converters, when a PaaS is the right 'orchestrator'.",
        },
    ],
    "whiteboard": [
        "Draw layers of a Python image after changing app.py vs requirements.txt.",
        "Network diagram: browser → host:8000 → api container → postgres container.",
        "Design a dev vs prod compose overlay.",
    ],
    "interview_listen": "layer cache, localhost vs service DNS, non-root, volumes",
    "cheatsheet": {
        "remember": "Service DNS not localhost. COPY reqs first. Non-root. Volumes for data. 0.0.0.0.",
        "bash": "docker compose up --build\ndocker compose logs -f api\ndocker compose down -v\ndocker build -t me/api:0.1 .\ndocker exec -it NAME bash",
        "python": "CMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]",
        "decisions": "Dev deps → compose. Prod single node → compose or PaaS. Multi node → orchestrator.",
        "numbers": "Slim Python images ~120MB+. Alpine can break manylinux wheels — slim-bookworm is safer.",
        "do_not": "latest in prod. secrets in layers. root. copy .venv. localhost to reach sibling containers.",
    },
    "miniproject": {
        "name": "compose-stack",
        "time": "1 day",
        "difficulty": "Medium",
        "why": "Take-homes that cannot docker compose up get skipped.",
        "story": "A teammate clones and is up in one command.",
        "must": ["Dockerfile", "compose api+pg+redis", "healthchecks", ".dockerignore", "non-root"],
        "should": ["multi-stage", "dev override compose"],
        "wont": ["Kubernetes"],
        "architecture": "```mermaid\nflowchart LR\nHost --> API --> PG\nAPI --> Redis\n```",
        "layout": "Dockerfile compose.yaml .dockerignore",
        "rubric": ["one command", "data persists", "README troubleshooting"],
        "stretch": "Add a Makefile with up/down/logs/psql.",
    },
    "resources": {
        "official": ["[Dockerfile best practices](https://docs.docker.com/develop/develop-images/instructions/)", "[Compose](https://docs.docker.com/compose/)"],
        "extra": ["[100-Days-Of-Docker](https://github.com/DARKANGEL689/100-Days-Of-Docker)", "dive (layer explorer)"],
        "papers": ["n/a"],
    },
    "faq": [
        {"q": "Podman?", "a": "Fine. Commands are similar. This course uses Docker names."},
        {"q": "Alpine or slim?", "a": "Debian slim for Python AI. Alpine's musl breaks many wheels."},
        {"q": "Do I need Kubernetes now?", "a": "No. Phase 11 mentions it. Compose is the skill."},
    ],
    "debugging": [
        {
            "title": "connection refused to postgres",
            "symptom": "API boots, DB errors.",
            "wrong": "DATABASE_URL uses localhost.",
            "see": "Print the URL (without password). docker compose exec api ping postgres.",
            "fix": "Hostname postgres. Wait for healthy.",
            "prevent": "compose depends_on condition + README.",
        },
        {
            "title": "Permission denied on volume",
            "symptom": "Non-root user cannot write.",
            "wrong": "Volume owned by root from an earlier run.",
            "see": "ls -l inside container.",
            "fix": "chown, or init container, or matching uid.",
            "prevent": "Document uids. Don't mix root and non-root writes.",
        },
    ],
    "mistakes": [
        {"title": "Bind-mounting the whole repo including host .venv", "body": "Linux container cannot use a macOS venv.", "instead": "Mount source only; install deps in the image. Or named volume for /app/.venv."},
        {"title": "apt-get without rm -rf /var/lib/apt/lists", "body": "Fat layers.", "instead": "Clean in the same RUN."},
        {"title": "Storing models in the image", "body": "Multi-GB images, slow deploys.", "instead": "Volume, object storage, or model sidecar."},
    ],
    "prod_tips": {
        "cost": "Image size is pull time which is deploy time which is money on CI minutes.",
        "latency": "Cold start = pull + boot. Smaller + fewer layers + min deps.",
        "reliability": "Healthchecks, restart: unless-stopped, pin tags.",
        "observability": "Logs to stdout. docker compose logs. Later: ship to a backend.",
        "scaling": "Compose scales poorly across machines. That's when Fly/ECS/K8s appear.",
        "checklist": ["dockerignore", "non-root", "pin tags", "health", "no secrets in image", "0.0.0.0"],
    },
    "challenge": {
        "title": "Reproduce CI locally",
        "body": "A GitHub Action builds the image and runs pytest inside it. Same command works locally.",
        "constraints": ["No extra undocumented env", "Python version matches"],
        "success": "A failing test fails in both places the same way.",
    },
    "solutions": [
        {"id": "B1 dockerignore", "hint": "docker build then docker run find /app/.venv — should miss.", "approach": "Add .venv to dockerignore."},
        {"id": "M1 health", "hint": "curl -f http://localhost:8000/healthz in HEALTHCHECK.", "approach": "Need curl in image or use python -c urllib."},
    ],
    "code_files": {
        "Dockerfile": """FROM python:3.12-slim
WORKDIR /app
RUN useradd --create-home --uid 1000 appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || true
COPY --chown=appuser:appuser . .
USER appuser
EXPOSE 8000
CMD ["python", "-m", "http.server", "8000"]
""",
        "compose.yaml": """services:
  api:
    build: .
    ports: ["8000:8000"]
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
  pgdata: {}
""",
        ".dockerignore": ".venv\n.git\n__pycache__\n*.pyc\n.env\n",
    },
}
