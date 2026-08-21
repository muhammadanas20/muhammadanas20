# Debugging — Phase 0: Developer setup

Debugging is the job. These are bugs we see every week.

## Bug 1. `python` opens the Microsoft Store

**Symptom**

Windows: typing python tries to install Python from the Store.

**Broken mental model**

Python is installed because you installed it once in 2021.

**How to see it**

`where python` and App execution aliases in Windows Settings.

**Fix**

Disable Store aliases. Install Python 3.12. Use `py -3.12`. In WSL, use Linux Python.

**Prevention**

Develop inside WSL. Document `py -3.12` for teammates stuck on Windows.
## Bug 2. ModuleNotFoundError after pip install

**Symptom**

You installed fastapi but Python cannot import it.

**Broken mental model**

pip and python are the same environment.

**How to see it**

`python -m pip --version` vs `pip --version` vs `sys.executable`.

**Fix**

Always `python -m pip install ...` using the venv interpreter.

**Prevention**

Never use a global pip. `uv run` also prevents this.
## Bug 3. Docker: Cannot connect to the Docker daemon

**Symptom**

CLI works, daemon doesn't.

**Broken mental model**

Docker is a single binary. It is a client plus a background engine.

**How to see it**

Is Docker Desktop running? `docker info`. On Linux, is your user in the `docker` group?

**Fix**

Start the engine. Log out/in after adding the group. Never `sudo docker` as a lifestyle.

**Prevention**

README: 'Start Docker Desktop first.'


## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
