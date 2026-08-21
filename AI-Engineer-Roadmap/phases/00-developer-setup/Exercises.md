# Exercises — Phase 0: Developer setup

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. Ignore the right things

Write a `.gitignore` that excludes `.venv/`, `.env`, `__pycache__/`, and `*.pyc` but NOT `.env.example`.

**Constraints:** No broad `*` that hides Python source.

### B2. Sanity script

Extend `sanity.py` to also print whether Docker is reachable (`docker info` via subprocess) without crashing if it is not.

**Constraints:** Exit 0 even if Docker is down; print a clear message.

## Medium

### M1. Makefile or justfile

Add `make setup` that creates venv and installs requirements, and `make sanity` that runs the probe.

**Constraints:** Works on macOS and Linux. Document Windows equivalent.

### M2. Pre-commit

Add `ruff` as a pre-commit hook so bad syntax cannot be committed.

**Constraints:** Hook runs in under 3 seconds on this repo slice.

## Hard

### H1. Devcontainer

Write a `.devcontainer/devcontainer.json` that uses Python 3.12, installs Docker-in-Docker or expects the host Docker socket, and auto-creates a venv.

**Constraints:** A classmate can Open in Container and run sanity.py.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase0/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
