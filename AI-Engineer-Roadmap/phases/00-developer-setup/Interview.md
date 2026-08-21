# Interview — Phase 0: Developer setup

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. What is a virtual environment and why should I care?

**Expected answer (junior)**

A directory with its own Python and packages so project A and B can depend on different versions. Without it, global installs collide.

**Common mistakes**

Saying 'it makes Python faster' or mixing it up with Docker / conda without knowing the difference.

**Senior-level discussion**

Talk about reproducibility, CI parity, and how lock files + venv beat 'pip install latest' on a laptop that has been alive since 2019.
### Q2. When do you reach for Docker vs a venv?

**Expected answer (junior)**

venv for Python libs. Docker when I need system packages, other services, or to match production Linux.

**Common mistakes**

Dockerizing every script. Or never using Docker and shipping 'install Postgres yourself' as a README.

**Senior-level discussion**

Devcontainers, multi-stage builds, and the cost of Docker on macOS file mounts. Also: not using Docker as a secrets manager.
### Q3. A teammate committed an API key. What do you do?

**Expected answer (junior)**

Rotate the key immediately. Remove it from the repo. Add .env to gitignore. Check Git history.

**Common mistakes**

Only deleting the file in a new commit and considering it solved.

**Senior-level discussion**

Incident: rotate, audit usage logs, purge history or treat the repo as compromised, add secret scanning (gitleaks, GitHub scanning), blameless postmortem.
### Q4. Explain WSL vs dual boot vs a Linux VM.

**Expected answer (junior)**

WSL2 is a lightweight Linux kernel on Windows. Dual boot is a full OS switch. A VM is heavier isolation.

**Common mistakes**

Claiming WSL is 'just an emulator' (WSL2 is a real kernel) or putting repos on /mnt/c.

**Senior-level discussion**

I/O performance, Docker Desktop backend, GPU passthrough limits, corporate policy.
### Q5. How do you make onboarding a 15-minute task?

**Expected answer (junior)**

README, .env.example, compose, one setup command, a sanity check.

**Common mistakes**

A 40-page Confluence novel and no compose file.

**Senior-level discussion**

Devcontainers or nix, golden images, seed data, a 'hello request' in CI that hits the stack.


---

## Whiteboard prompts

- Draw how a Python process finds a package (PATH, venv, site-packages).
- Sketch a laptop → GitHub → Actions → runner path and mark where secrets live.
- A Windows teammate is slow in WSL. Diagnose.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for calm hygiene: venvs, secrets, Linux CI, and no cargo-cult Docker.
