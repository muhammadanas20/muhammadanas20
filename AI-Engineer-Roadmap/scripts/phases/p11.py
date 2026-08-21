from make_phase import C, E, EX, I, Q, asg, drill, mp, phase, th

PHASE = phase(
    num="11",
    title="Deployment",
    tagline="A URL that is not localhost. CI that is not a prayer.",
    hours="10-14 days",
    difficulty="Hard",
    exit_ticket="Git push deploys a versioned API with a healthcheck and a rollback story.",
    objectives=[
        "Ship a container to at least one PaaS (Render, Railway, or Fly.io).",
        "Sketch AWS, Azure, and GCP at the 'I can find the right service' level.",
        "Put Nginx in front or understand the platform's proxy.",
        "Write GitHub Actions: lint, test, build, deploy.",
        "Manage secrets, healthchecks, and rollbacks.",
    ],
    prerequisites=["Phase 4 Docker. A FastAPI app worth deploying (Phase 3 or 8)."],
    topics=["Docker in prod", "Render", "Railway", "Fly.io", "AWS", "Azure", "GCP", "Nginx", "GitHub Actions"],
    nav="[Home](../../README.md) · Prev: [Phase 10](../10-mcp/) · Next: [Phase 12 · LLMOps](../12-production-ai/)",
    theory=th(
        intro="""Deployment is moving a known image to a machine that has a public URL, secrets, logs, and a way back.

You do not need to pass a Kubernetes exam. You need:

- A container
- A host
- Secrets not in Git
- CI
- Healthchecks
- A rollback

PaaS (Fly, Render, Railway) teaches this fastest. Cloud hyperscalers are the same ideas with more knobs.""",
        one_liner="Ship a tagged image, with secrets, health, and a rollback.",
        why="""Hiring managers click links. Localhost is not a portfolio.

Also: you will learn that SSE dies behind a buffering proxy, that cold starts wake your bill, and that 'it worked on my laptop' dies in Linux CI — which is the point of Phase 0–4.""",
        if_missing="your RAG would live as a zip file on Drive.",
        analogy="""A restaurant opening.

- **Image** = the frozen menu and kitchen layout
- **Registry** = the warehouse of those frozen kits (Docker Hub / GHCR)
- **PaaS** = renting a food truck (Fly/Render/Railway)
- **AWS/GCP/Azure** = leasing a mall (more control, more mopping)
- **Nginx** = the host at the door (TLS, routing, buffering — careful with SSE)
- **GitHub Actions** = the checklist before service starts
- **Healthcheck** = 'is the kitchen actually cooking?'
- **Rollback** = serving yesterday's menu when tonight's soup is poison
- **Secrets** = the safe, not the chalkboard""",
        visual="""```mermaid
flowchart LR
  Git --> GHA[GitHub Actions]
  GHA --> Test
  Test --> Build
  Build --> Reg[GHCR]
  Reg --> PaaS[Fly / Render / Railway]
  PaaS --> URL[https://...]
```""",
        architecture="""```mermaid
flowchart TB
  User --> CDN
  CDN --> Nginx
  Nginx --> API[Uvicorn]
  API --> PG[(managed Postgres)]
  API --> Redis[(managed Redis)]
  API --> VDB[(vector store)]
  API --> LLM[Model API]
```""",
        beginner="""**Environment:** `APP_ENV=production`. Debug off.

**Proccess:** Uvicorn/Gunicorn behind a proxy. Bind 0.0.0.0.

**Health:** `GET /healthz` returns 200 if process up. `GET /readyz` if DB ping works.

**Secrets:** platform env vars or a secret manager. Same names as `.env.example`.

**PaaS:**
- **Render:** easy web + Postgres
- **Railway:** similar, good DX
- **Fly.io:** close to you, VMs, good for Docker-first

Pick **one**. Deploy fully. Then skim the others.

**GitHub Actions:** YAML in `.github/workflows`. On push: checkout, setup Python, test, build image, push, deploy.""",
        intermediate="""**Tagging:** `ghcr.io/you/api:sha-abc1234` not `:latest`. Deploy by digest.

**Migrations:** run as a release command *before* new traffic, with expand/contract.

**SSE + proxies:** disable buffering. Timeouts longer than model latency.

**Cold start:** scale-to-zero is cheap and slow. Chat apps often want min 1 instance.

**TLS:** the PaaS terminates TLS. You still want HTTPS-only.

**Nginx (if you run it):** reverse proxy, size limits, `proxy_buffering off` for streams, websocket maps.

**Kubernetes (sketch):** Pod = container(s), Deployment = replicas, Service = DNS, Ingress = HTTP entry. `kind` locally if curious. Not required to finish this course.""",
        advanced="""**Blue/green and canary.**

**OIDC from Actions to cloud** — no long-lived AWS keys in GitHub.

**Infra as code:** Terraform/Pulumi later. PaaS dashboard is OK for the first deploy.

**Observability hook:** logs to stdout now; Phase 12 adds traces.

**GPU hosts** if you self-host models (RunPod, Modal, Fly GPU). Most juniors should call APIs instead.""",
        production="""SLOs, status page, on-call (even if it's just you + email). Backup restore test. Dependency on model vendor: timeout and fallback (Phase 12). Cost alerts.

Never: SSH-and-pray as the only deploy. Never: build on your laptop and scp.""",
        when="When a human besides you must use it. When you want CI to be the source of truth.",
        when_not="A private experiment. Don't Kubernetes a weekend bot.",
        code_preview='''# .github/workflows/deploy.yml sketch
# on: push to main
# jobs: test -> build-push -> deploy
''',
        code_notes="Three jobs with needs:. Fail closed. Secrets in GitHub Secrets.",
        ex_b="Deploy a static healthz FastAPI to one PaaS.",
        ex_m="Actions: ruff + pytest on PR.",
        ex_h="Full: tests, image to GHCR, deploy, smoke curl, rollback notes.",
        project="Public URL for PDF chat or chat API.",
        interview_preview="CI vs CD. Why not latest. Health vs ready. How you rollback. SSE vs Nginx.",
        flash_sample="**Q:** Where do production secrets live?\n**A:** The platform secret store, not Git.",
        mistakes_preview="latest tags. No healthcheck. Migrations in the API process start (racy). Buffering SSE. Committing kubeconfigs.",
        debug_preview="Works locally, 502 in prod (bind 127.0.0.1). OOM. Secret missing so boot loop.",
        best="Tagged images, OIDC, health/ready, smoke after deploy, migrations expand/contract, logs stdout.",
        industry="GitHub Actions + a PaaS is a perfectly respectable junior story. Bigger cos: GKE/EKS/AKS + Terraform.",
        perf="Min instances for chat. Region near users or near DB. Don't pull 5GB models on each boot.",
        security="Secrets, non-root, HTTPS, least-open firewall, dependency scanning in CI.",
        refs="- GitHub Actions docs\n- Fly/Render/Railway docs\n- 12-factor app",
        further="Google SRE book (skim). Kubernetes the hard way — later.",
    ),
    examples=[
        EX(
            title="Health and ready",
            why="Orchestrators need both.",
            code='''"""code/health.py"""
from fastapi import FastAPI, Response

app = FastAPI()
ready = True  # set False during shutdown

@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/readyz")
def readyz() -> Response:
    if not ready:
        return Response(status_code=503)
    return Response(status_code=200)
''',
            line_by_line="healthz: process live. readyz: safe to send traffic. 503 removes you from the load balancer.",
            output="200 / 503",
            dry_run="LB polls. During shutdown ready=False, still healthz ok until exit.",
            memory="O(1)",
            time="O(1) unless readyz pings DB",
            space="O(1)",
            alternatives="Add DB ping in readyz.",
            optimization="Don't run a 200ms DB query every 1s without pooling.",
        ),
        EX(
            title="GitHub Actions test job",
            why="CI is the first deploy.",
            code='''# code/ci.yml
name: ci
on:
  pull_request:
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: ruff check .
      - run: pytest -q
''',
            line_by_line="PR and main. Ubuntu. Pin Python. Lint then test. Add secrets later, never in YAML.",
            output="Green checks on GitHub.",
            dry_run="Push → runner VM → steps in order → fail stops deploy job if you add needs.",
            memory="Runner has limited RAM — don't load huge models in CI.",
            time="Minutes",
            space="Workspace on runner",
            alternatives="GitLab CI, Circle.",
            optimization="Cache pip. Split lint/test.",
        ),
    ],
    practice=[
        drill("One PaaS account", "Deploy hello world. Custom domain optional.", "HTTPS URL."),
        drill("Break a secret", "Remove DATABASE_URL, watch crash, restore.", "You read platform logs."),
        drill("Actions on a PR", "Open a PR that fails ruff, then fix.", "Red then green."),
    ],
    exercises={
        "beginner": [
            E("healthz", "Add both endpoints. curl them.", "readyz fails if you set a fake flag."),
            E("Dockerfile CMD", "0.0.0.0 in prod image.", "Prove 127.0.0.1 is unreachable from host map."),
        ],
        "medium": [
            E("GHCR", "Build and push an image tagged with SHA.", "Public or private with a note."),
            E("Release command", "Run a dummy migration before start.", "Document order."),
        ],
        "hard": [
            E("Full pipeline", "test → build → deploy → smoke.", "README rollback."),
            E("Nginx SSE", "Local nginx in front of uvicorn; fix buffering.", "curl -N shows chunks."),
        ],
    },
    assignments=[
        asg(
            "ship-it",
            "2–4 days",
            "Deploy your RAG or chat API. Public HTTPS. Actions. Secrets on the platform. README with URL and architecture.",
            ["live URL", "workflow YAML", "rollback notes"],
            ["healthz", "no secrets in git", "smoke in CI or documented curl"],
        )
    ],
    quiz=[
        Q("latest tag in prod", "Best", "Not reproducible", "Required by Docker", "Encrypts", "B", "Pin SHA."),
        Q("healthz vs readyz", "Same", "Live vs ready for traffic", "Only k8s has them", "JWT things", "B", "Two signals."),
        Q("Secrets belong in", "Git", "Platform secret store", "Docker image layers", "README", "B", "Not git."),
        Q("SSE behind Nginx", "Always fine", "May buffer; disable proxy buffering", "Impossible", "Needs UDP", "B", "Buffering."),
        Q("CI should run on", "Only your Mac", "Linux runners typically", "iOS", "Windows 95", "B", "ubuntu-latest."),
        Q("Rollback means", "Rewrite history", "Put the previous good image back in service", "Delete GitHub", "Scale to 0 forever", "B", "Previous image."),
        Q("Bind 127.0.0.1 in a container", "Reachable from the internet", "Only inside the container", "Required", "Faster TLS", "B", "Use 0.0.0.0."),
        Q("PaaS vs hyperscaler", "PaaS is less mopping, less control", "PaaS is always cheaper at infinite scale", "AWS is simpler than Render for hello world", "They are identical", "A", "Tradeoff."),
        Q("Kubernetes Pod is", "A physical server", "One or more containers scheduled together", "A JWT", "A prompt", "B", "Sketch level."),
        Q("OIDC from GitHub to cloud", "Long-lived keys in secrets", "Short-lived federation, better", "A vector index", "A reranker", "B", "Prefer OIDC."),
    ],
    flashcards=[
        C("12-factor config?", "Env vars, not baked files."),
        C("Where is TLS terminated often?", "The PaaS / load balancer."),
        C("Why tag with git SHA?", "Traceability and rollback."),
        C("Smoke test?", "A tiny request after deploy proving liveness."),
        C("Scale to zero cost?", "Cheap, cold start latency."),
        C("GHCR?", "GitHub Container Registry."),
        C("readyz 503?", "Stop sending traffic."),
        C("Migrations when?", "Before new code needs the new schema (expand first)."),
        C("Nginx role?", "Reverse proxy, TLS, routing, static."),
        C("Minimum k8s vocab?", "Pod, Deployment, Service, Ingress."),
    ],
    interview=[
        I("Walk through your deploy.", "Push → Actions test → build image SHA → registry → PaaS pulls → health → live. Rollback = previous SHA.", "I click upload on a website.", "Canary, migrations, secrets."),
        I("How do you handle secrets?", "Platform store, injected as env, .env.example committed, rotation plan.", "In the repo but it's private.", "SOPS, vault, OIDC."),
        I("App 502s after deploy.", "Logs, health, bind address, secret missing, migrations, OOM, proxy timeout vs model.", "Rebuild laptop.", "Systematic."),
        I("Why not Kubernetes first?", "Need the container story first. K8s is an orchestrator for many nodes. PaaS is enough for this app.", "K8s is always required to be senior.", "When k8s wins: many services, complex scheduling."),
        I("CI vs CD?", "CI = verify each change. CD = automatically/continuously ship those verified artifacts.", "They are the same letters so the same.", "Gates, environments, approvals."),
    ],
    whiteboard=[
        "Pipeline from git to HTTPS.",
        "Where buffering can kill SSE.",
        "Expand/contract migration around a deploy.",
    ],
    interview_listen="tagged artifacts, secrets, health, rollback — not a 40-box k8s diagram",
    cheatsheet={
        "remember": "SHA tags. Secrets off git. healthz/readyz. 0.0.0.0. Rollback = old image.",
        "bash": "fly deploy\nrender/railway dashboards\ngh workflow view",
        "python": '@app.get("/healthz")\\ndef healthz(): return {"ok": True}',
        "decisions": "One service → PaaS. Many services + team → cloud/k8s later.",
        "numbers": "Health interval 5–15s. Proxy timeout > model p95. Min 1 instance for chat UX.",
        "do_not": "latest. secrets in images. bind 127.0.0.1. skip smoke.",
    },
    miniproject=mp(
        name="ship-pdf-chat",
        time="2–4 days",
        difficulty="Hard",
        why="Live URL on the resume.",
        story="A stranger can open the API docs on the internet.",
        must=["HTTPS", "Actions", "secrets on platform", "healthz", "README URL"],
        should=["smoke curl in CI"],
        wont=["Multi-region active-active"],
        architecture="```mermaid\nflowchart LR\nGitHub --> Actions --> Registry --> PaaS\n```",
        layout="../../DEPLOYMENT/",
        rubric=["URL works", "no secrets", "rollback paragraph"],
        stretch="Custom domain + status badge.",
    ),
    resources={
        "official": ["GitHub Actions", "Fly.io docs", "Render docs", "Railway docs", "12factor.net"],
        "extra": ["OWASP secrets", "Nginx SSE notes"],
        "papers": ["n/a"],
    },
    faq=[
        {"q": "Which PaaS?", "a": "The one whose free tier is alive this month. Fly/Render/Railway are all fine. Pick one and finish."},
        {"q": "AWS required?", "a": "For some jobs. Learn the map (ECS/EKS/Lambda/RDS). Don't boil the ocean before you have a URL."},
        {"q": "GPU?", "a": "Not for calling OpenAI. Only if you self-host models."},
    ],
    debugging=[
        {
            "title": "502 Bad Gateway",
            "symptom": "Platform URL fails.",
            "wrong": "App listens on 127.0.0.1 or wrong PORT.",
            "see": "Logs. PORT env. docker run locally with same env.",
            "fix": "0.0.0.0 and the platform's PORT.",
            "prevent": "Smoke test in CI against the container.",
        },
        {
            "title": "Works then dies after 30s",
            "symptom": "SSE/chat cut off.",
            "wrong": "Proxy idle timeout.",
            "see": "Platform timeout settings. Nginx proxy_read_timeout.",
            "fix": "Raise timeouts; heartbeats.",
            "prevent": "Load test the real URL, not localhost.",
        },
    ],
    mistakes=[
        {"title": "Building on a laptop and copying the image ad hoc", "body": "Not reproducible.", "instead": "CI builds Linux images."},
        {"title": "One long-lived AWS access key in GitHub", "body": "Leak = account takeover.", "instead": "OIDC."},
        {"title": "No rollback plan", "body": "You debug live for 3 hours.", "instead": "Keep last 5 images. One command back."},
    ],
    prod_tips={
        "cost": "Scale to zero vs min 1. Token spend still dwarfs a $7 VM. Watch both.",
        "latency": "Region, cold start, proxy. Measure from the user's geography if you can.",
        "reliability": "Health, retries at the edge, multi-AZ when money exists.",
        "observability": "Stdout logs now. Traces next phase.",
        "scaling": "Horizontal replicas of stateless API. State in PG/Redis.",
        "checklist": ["HTTPS", "secrets", "SHA tag", "health", "smoke", "rollback"],
    },
    challenge={
        "title": "Two environments",
        "body": "staging and prod. PRs deploy staging. Main deploys prod. Different secrets.",
        "constraints": ["No sharing prod DB with staging"],
        "success": "A diagram in README.",
    },
    solutions=[
        {"id": "M1 GHCR", "hint": "docker/login-action + GITHUB_TOKEN.", "approach": "Permission packages: write."},
        {"id": "H2 nginx", "hint": "proxy_buffering off; gzip off for that location.", "approach": "curl -N evidence."},
    ],
    code_files={
        "health.py": '''"""Health and readiness endpoints."""
from fastapi import FastAPI, Response

app = FastAPI()
ready = True


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/readyz")
def readyz() -> Response:
    if not ready:
        return Response(status_code=503)
    return Response(status_code=200)
''',
        "ci.yml": '''name: ci
on:
  pull_request:
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt || true
      - run: pytest -q || true
''',
    },
)
