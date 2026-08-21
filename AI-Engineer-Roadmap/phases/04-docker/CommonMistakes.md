# Common mistakes — Phase 4: Docker

### 1. Bind-mounting the whole repo including host .venv

Linux container cannot use a macOS venv.

**Do this instead:** Mount source only; install deps in the image. Or named volume for /app/.venv.

### 2. apt-get without rm -rf /var/lib/apt/lists

Fat layers.

**Do this instead:** Clean in the same RUN.

### 3. Storing models in the image

Multi-GB images, slow deploys.

**Do this instead:** Volume, object storage, or model sidecar.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
