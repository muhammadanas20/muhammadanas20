# FAQ — Phase 0: Developer setup

### Do I have to use Linux?

No. macOS is excellent. Windows + WSL2 is the supported Windows path. Native Windows without WSL will fight Docker and Unix tutorials.

### Conda or venv?

venv/uv for this course. Conda is fine in data-science shops; mixing conda + pip + Docker blindly is how environments rot.

### Cursor / Windsurf / Neovim instead of VS Code?

Yes. You still need a terminal, a Python interpreter picker, and Docker. The editor is not the skill.

### I don't have admin rights on my laptop.

Use user-level installs, pyenv/uv in home, or a cloud devbox (GitHub Codespaces). Document the constraint.

### Is Docker Desktop paid?

Docker Inc. has license rules for large companies. As a student, Docker Desktop or Engine + Compose V2 is fine. Colima or Podman are alternatives on macOS/Linux.

Didn't see your question? Open an issue. Beginner questions are first-class.
