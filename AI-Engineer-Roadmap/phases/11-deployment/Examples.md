# Examples — Phase 11: Deployment

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. Health and ready

Orchestrators need both.

```python
"""code/health.py"""
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

```

**What every interesting line is doing**

healthz: process live. readyz: safe to send traffic. 503 removes you from the load balancer.

**Expected output**

```text
200 / 503
```

**Dry run**

LB polls. During shutdown ready=False, still healthz ok until exit.

**Memory**

O(1)

**Time complexity:** O(1) unless readyz pings DB  
**Space complexity:** O(1)

**Alternatives**

Add DB ping in readyz.

**Optimization**

Don't run a 200ms DB query every 1s without pooling.

---

### Example 2. GitHub Actions test job

CI is the first deploy.

```python
# code/ci.yml
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

```

**What every interesting line is doing**

PR and main. Ubuntu. Pin Python. Lint then test. Add secrets later, never in YAML.

**Expected output**

```text
Green checks on GitHub.
```

**Dry run**

Push → runner VM → steps in order → fail stops deploy job if you add needs.

**Memory**

Runner has limited RAM — don't load huge models in CI.

**Time complexity:** Minutes  
**Space complexity:** Workspace on runner

**Alternatives**

GitLab CI, Circle.

**Optimization**

Cache pip. Split lint/test.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
