# Solutions — Phase 4: Docker

Spoilers. Try for 25 minutes first.

We give **hints and approaches**, not copy-paste repos. If you paste a full solution into your portfolio without understanding it, the interview will hurt.

### B1 dockerignore

docker build then docker run find /app/.venv — should miss.

<details><summary>Approach (still not full code)</summary>

Add .venv to dockerignore.

</details>

### M1 health

curl -f http://localhost:8000/healthz in HEALTHCHECK.

<details><summary>Approach (still not full code)</summary>

Need curl in image or use python -c urllib.

</details>

Full working patterns related to this phase also live in [`code/`](./code/) and [EXAMPLES](../../EXAMPLES/).
