# Interview — Phase 4: Docker

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. Walk me through a good Python Dockerfile.

**Expected answer (junior)**

Slim base, workdir, copy requirements, pip, copy app, non-root, CMD uvicorn 0.0.0.0, dockerignore.

**Common mistakes**

FROM python:latest, run as root, pip as a separate surprise every build.

**Senior-level discussion**

Multi-stage, hash pins, SBOM, distroless tradeoffs, BuildKit caches, non-root + writable /tmp.
### Q2. App cannot reach Postgres in Compose.

**Expected answer (junior)**

They're using localhost. Should use hostname postgres. Also wait for healthy.

**Common mistakes**

Reinstall Docker as first step.

**Senior-level discussion**

Networks, multiple compose files, IPv6, pg_hba, password env mismatch.
### Q3. Image vs VM?

**Expected answer (junior)**

Containers share the host kernel; VMs virtualize hardware. Containers start faster and are denser.

**Common mistakes**

Containers are 'just VMs'.

**Senior-level discussion**

Isolation limits, noisy neighbor, Windows containers vs Linux, when VMs still win (hostile multi-tenant).
### Q4. How do you keep images small?

**Expected answer (junior)**

Slim base, no-cache pip, dockerignore, multi-stage, combine RUN, no extra apt.

**Common mistakes**

Delete files in a later layer and expect size to drop fully (whiteout still costs unless squashed).

**Senior-level discussion**

dive to inspect layers, distroless, compressing wheels, not baking models into images.
### Q5. Is Compose production-ready?

**Expected answer (junior)**

Great for single-node and small deploys. For multi-node, use a scheduler (Fly, ECS, K8s).

**Common mistakes**

Compose is only for demos / Compose is enough for Netflix.

**Senior-level discussion**

Compose in CI, Swarm (rare), kube compose converters, when a PaaS is the right 'orchestrator'.


---

## Whiteboard prompts

- Draw layers of a Python image after changing app.py vs requirements.txt.
- Network diagram: browser → host:8000 → api container → postgres container.
- Design a dev vs prod compose overlay.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for layer cache, localhost vs service DNS, non-root, volumes.
