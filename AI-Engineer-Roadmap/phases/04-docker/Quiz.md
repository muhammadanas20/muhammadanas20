# Quiz — Phase 4: Docker

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

1. An image is:
    A) A running process
    B) An immutable snapshot/recipe result
    C) A volume
    D) A JWT
2. localhost inside a container is:
    A) The host machine
    B) That container
    C) Docker Hub
    D) Postgres always
3. COPY reqs then pip then COPY code:
    A) Stupid
    B) Enables layer cache for deps
    C) Required by Python
    D) Insecure
4. Named volumes are for:
    A) Source code usually
    B) Persistent data like PG
    C) JWTs
    D) DNS
5. 0.0.0.0 means:
    A) Listen on all interfaces
    B) Disable network
    C) IPv6 only
    D) Localhost only
6. compose down -v:
    A) Removes volumes too
    B) Updates Python
    C) Pushes images
    D) Is a no-op
7. Running as root in a container:
    A) Best practice
    B) Increases blast radius if escaped
    C) Required for Python
    D) Faster
8. .dockerignore should include:
    A) .venv and .git
    B) Only .py files
    C) Dockerfile
    D) requirements.txt
9. Healthcheck vs started:
    A) Same
    B) Healthy means the app is ready, not just the process spawned
    C) Healthcheck is for images only
    D) Compose cannot wait
10. :latest tag in prod:
    A) Recommended
    B) Not reproducible
    C) A security feature
    D) Faster deploys always

---

<details>
<summary>Answers (spoiler)</summary>

1. **B** — Container is the running instance.
2. **B** — Use service names.
3. **B** — Cache.
4. **B** — Data.
5. **A** — Needed in containers.
6. **A** — Data loss if you needed it.
7. **B** — Drop privileges.
8. **A** — Keep context small.
9. **B** — depends_on condition.
10. **B** — Pin versions.

</details>
