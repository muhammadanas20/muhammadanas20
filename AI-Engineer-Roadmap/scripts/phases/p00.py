PHASE = {
    "num": "0",
    "title": "Developer setup",
    "tagline": "A boring, reliable machine is a career skill. Flashy ricing is not.",
    "hours": "2-4 days",
    "difficulty": "Easy",
    "exit_ticket": "Clone this repo, create a venv with uv or pip, run a FastAPI hello-world in Docker, and push a branch to GitHub.",
    "objectives": [
        "Install a Unix-like environment (Linux, macOS, or Windows + WSL2) and use the terminal without fear.",
        "Use VS Code (or a fork) with Python, Docker, and EditorConfig extensions.",
        "Perform the Git loop: branch, commit, push, pull request, `.gitignore`.",
        "Create isolated Python environments with `venv` and `uv`.",
        "Run Docker Desktop (or Engine) and `docker compose`.",
        "Export environment variables without ever committing secrets.",
    ],
    "prerequisites": [
        "You can install software on your computer (admin rights).",
        "You have used Python at least a little.",
        "A GitHub account.",
    ],
    "topics": [
        "Linux / WSL / macOS realities",
        "Terminal: pipes, exit codes, env vars",
        "VS Code",
        "Git",
        "Python 3.11+, venv, uv",
        "Docker Desktop",
        "Secrets hygiene",
    ],
    "nav": "[Home](../../README.md) · [Roadmap](../../ROADMAP.md) · Next: [Phase 1 · Python refresh](../01-python-refresh/)",
    "theory": {
        "intro": """You cannot learn AI engineering on a machine that fights you.

Phase 0 is not "install some apps." It is the contract between you and every later phase:

- Python versions do not collide.
- Dependencies of project A cannot break project B.
- Docker behaves the same on your laptop and in CI.
- Secrets never sit in Git.
- You can explain what a process, a port, and an environment variable are.

If this feels too basic, take the quiz anyway. Many juniors who "know Python" cannot activate a venv inside WSL.""",
        "one_liner": "Make the computer boring so the models can be interesting.",
        "why": """Every production outage story that starts with "it worked on my machine" is a Phase 0 failure.

AI projects make this worse:

- Native wheels (NumPy, tokenizers, `psycopg`) care about OS and CPU.
- Docker images that "kind of work" on Apple Silicon surprise you on Linux CI.
- A leaked OpenAI key in a public repo can cost real money in an afternoon.

Companies hire people who can onboard onto a repo in 30 minutes. That skill is this phase.""",
        "if_missing": "you would spend Phase 8 debugging CUDA on Windows instead of retrieval quality.",
        "analogy": """Think of a professional kitchen.

The chef does not keep spices in a coat pocket. There is a station, labeled containers, a fire extinguisher, and a rule: do not store raw chicken next to dessert.

Your machine is the kitchen.

- **venv / uv** = labeled containers (this soup does not share a pot with that sauce).
- **Git** = recipes with versions.
- **Docker** = a lunch box that tastes the same on the train.
- **`.env`** = the safe. Not the recipe card.
- **WSL** (on Windows) = building the kitchen on the same floor plan as the restaurant (Linux).""",
        "visual": """```mermaid
flowchart LR
  subgraph host [Your computer]
    OS[Linux / macOS / WSL2]
    PY[Python 3.11+]
    UV[uv / venv]
    GIT[Git]
    DK[Docker engine]
  end
  subgraph project [One repo]
    ENV[.venv]
    DOT[.env not committed]
    CMP[compose.yaml]
  end
  OS --> PY --> UV --> ENV
  OS --> GIT
  OS --> DK --> CMP
  DOT -.->|read at runtime| ENV
```""",
        "architecture": """```mermaid
flowchart TB
  Dev[You in VS Code] --> Term[Integrated terminal]
  Term --> Venv[.venv interpreter]
  Venv --> App[Python app]
  App --> EnvFile[.env]
  App --> Docker[Optional: app inside a container]
  Docker --> Net[localhost ports]
  Git[Git branch] --> GH[GitHub]
  GH --> CI[GitHub Actions on Linux]
```

Notice CI runs **Linux**. If you only ever run on Windows without WSL, you will discover bugs at the worst time.""",
        "beginner": """**Terminal.** A program that sends text commands to the operating system. You type `ls` (or `dir` on old Windows) and it lists files. The number it returns is the **exit code**: `0` means success, anything else means failure. Pipelines (`|`) send the output of one command into the next.

**Path.** Where a file lives. `~/work/repo` is a folder. Spaces in paths will hurt you; avoid them.

**Process and port.** When you run an API it becomes a process listening on a port (Uvicorn likes `8000`). Only one process can bind a port. "Address already in use" means something else got there first.

**Environment variable.** A name-value pair visible to a process, like `OPENAI_API_KEY`. Apps read these so secrets are not hard-coded.

**Python version.** `python --version` must be 3.11 or 3.12 for this course. 3.10 will mostly work. 2.7 is a museum.

**Virtual environment.** A folder (`.venv`) with its own `python` and `site-packages`. Activate it so `which python` points inside the project.

**uv.** A fast modern tool that can create venvs and install packages. Optional but recommended. `pip` is fine.

**Git.** A history of your files. `commit` is a snapshot. `branch` is a line of work. GitHub is a host for those snapshots.

**Docker.** A way to run a lightweight, isolated Linux environment defined by a `Dockerfile`. Compose runs several containers together (app + database).""",
        "intermediate": """**WSL2.** Windows Subsystem for Linux runs a real Linux kernel next to Windows. Put your repos *inside* the Linux filesystem (`~/`), not `/mnt/c/...`, or Git and file-watchers will be slow and weird.

**Line endings.** Windows likes `CRLF`. Linux likes `LF`. Git can convert them and cause fake diffs. Set `core.autocrlf` appropriately or use EditorConfig (`end_of_line = lf`).

**pyproject.toml vs requirements.txt.** This course ships `requirements.txt` for simplicity. Production teams often use `pyproject.toml` + lock files (`uv.lock`, `poetry.lock`). A lock file pins exact versions so Tuesday's install matches Monday's.

**Multi-interpreter VS Code.** Always pick the interpreter from `.venv`. The bottom-right of VS Code lies if you do not look.

**Docker vs venv.** Use a venv for daily coding. Use Docker when you need Postgres, Redis, or a deploy-shaped environment. Do not Dockerize `print("hello")` on day one just to feel senior.

**PATH.** The list of folders the shell searches for programs. If `docker` is "not found," it is not installed *or* not on PATH.""",
        "advanced": """**Reproducible toolchains.** `uv python install 3.12` pins an interpreter. Nix and `asdf` exist; you do not need them yet. You *do* need to write the Python version in README.

**Devcontainers.** `.devcontainer/` lets VS Code open the repo inside Docker. Great for teams. Learn after you can write a Dockerfile by hand, or you will not be able to debug the container.

**Signing commits.** GPG or SSH signing proves a commit came from you. Optional here. Some companies require it.

**Credential helpers.** Never embed a GitHub password. Use SSH keys or `gh auth login`.

**File watchers and inotify** on large `node_modules` or `.venv` can melt laptops. Exclude them.

**Apple Silicon.** Docker images must support `linux/arm64` or you emulate (`platform: linux/amd64`) and go slow. Prefer official multi-arch images.""",
        "production": """On a team, "setup" is **onboarding time**. A good repo has:

- README with three commands to run
- `.env.example` with every key named
- `compose.yaml` for dependencies
- A known Python version
- CI that installs the same way
- Pre-commit or a formatter so style is not a debate

You will be judged in week one on whether you can clone and run, not on whether you know GraphRAG.

**When you join a company:** read their onboarding doc. Do not invent a parallel toolchain. Match theirs.""",
        "when": "Always. Every project. Every laptop. Every CI runner.",
        "when_not": "Do not spend a week ricing zsh themes before Phase 1. Do not install Kubernetes because a Twitter thread said so. Do not dual-boot five distros.",
        "code_preview": '''"""Tiny sanity check you will run in every new environment."""
import platform
import sys
from pathlib import Path

print("python", sys.version)
print("executable", sys.executable)
print("platform", platform.platform())
print("in_venv", sys.prefix != sys.base_prefix)
print("cwd", Path.cwd())
''',
        "code_notes": """- `sys.executable` must point at `.venv` after activation.
- `in_venv` should print `True`. If not, you installed packages onto your system Python. That is how machines rot.""",
        "ex_b": "Print Python version, confirm venv, create a Git repo, write a `.gitignore` that excludes `.venv` and `.env`.",
        "ex_m": "Write a `compose.yaml` that runs `nginx:alpine` and serves a static `index.html` on port 8080.",
        "ex_h": "Create a GitHub Actions workflow that runs on Ubuntu, sets up Python 3.12, installs requirements, and executes `python code/sanity.py`.",
        "project": "A personal `dotfiles-lite` plus an `ai-eng-lab` repo with README, venv instructions, and a passing Actions workflow. See MiniProject.md.",
        "interview_preview": "What is a virtual environment? Why not install globally? What does Docker add that venv does not? How do you keep secrets out of Git?",
        "flash_sample": "**Q:** Exit code of a successful command?\n**A:** 0.",
        "mistakes_preview": "Installing packages without activating the venv. Committing `.env`. Developing on `/mnt/c` inside WSL. Using Python 3.9 because it was already there.",
        "debug_preview": "`python` on Windows pointing at the Store stub. Docker daemon not running. Port 8000 taken. Git refusing to commit because user.name is unset.",
        "best": """- One Python per project, isolated.
- `LF` line endings.
- `.env.example` committed, `.env` never.
- README says the exact Python version.
- Format with `ruff` so you stop arguing about quotes.""",
        "industry": """Teams use: VS Code or JetBrains, GitHub/GitLab, a lock file, Docker for services, a secrets manager (1Password, Doppler, AWS SM) — not a spreadsheet of keys.

`uv` is rapidly becoming the default installer in 2025–2026 Python shops. Know `pip` too.""",
        "perf": "Put code on the native filesystem (not `/mnt/c`). Exclude `.venv` from antivirus and from VS Code file watchers. Use `uv` if `pip install` is the slow part of your day.",
        "security": """Never commit secrets. Rotate a key if it leaked even for a minute. Do not paste keys into ChatGPT. SSH keys need passphrases. Disk encryption on laptops is not optional if you have customer data later.""",
        "refs": """- [Python venv docs](https://docs.python.org/3/library/venv.html)
- [uv](https://docs.astral.sh/uv/)
- [Git book, chapters 1–3](https://git-scm.com/book/en/v2)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [WSL docs](https://learn.microsoft.com/windows/wsl/)""",
        "further": """- [100 Days of Docker](https://github.com/DARKANGEL689/100-Days-Of-Docker) if you want extra drills after Phase 4
- [free-programming-books](https://github.com/EbookFoundation/free-programming-books) for your language""",
    },
    "examples_intro": "These examples are small on purpose. The skill is *running them in the right environment.*",
    "examples": [
        {
            "title": "Detect the interpreter (never guess)",
            "why": "Half of 'module not found' bugs are the wrong Python.",
            "code": '''"""code/sanity.py — run after activating .venv"""
import sys
from pathlib import Path

def main() -> None:
    # sys.prefix is the environment prefix (.venv)
    # sys.base_prefix is the interpreter that created it
    in_venv = sys.prefix != sys.base_prefix
    print(f"executable={sys.executable}")
    print(f"version={sys.version.split()[0]}")
    print(f"in_venv={in_venv}")
    print(f"cwd={Path.cwd()}")
    if not in_venv:
        # Non-zero exit so CI can fail
        raise SystemExit("Activate .venv first")

if __name__ == "__main__":
    main()
''',
            "line_by_line": """- `sys.prefix != sys.base_prefix` is the reliable venv check.
- `SystemExit` with a message sets exit code 1.
- `if __name__ == "__main__"` stops this from running during imports.""",
            "output": "executable=/home/you/repo/.venv/bin/python\nversion=3.12.x\nin_venv=True\ncwd=/home/you/repo",
            "dry_run": "Python starts → imports sys → compares prefixes → prints four lines → exits 0. If prefixes match, raises SystemExit, shell shows a non-zero status.",
            "memory": "Tiny. A few strings. No leaks. This is a probe, not an app.",
            "time": "O(1)",
            "space": "O(1)",
            "alternatives": "`uv run python code/sanity.py` runs inside the project's environment without manual activate.",
            "optimization": "None needed. Do not wrap this in Docker.",
        },
        {
            "title": "Read secrets from the environment, never from source",
            "why": "The first production-shaped habit.",
            "code": '''"""code/env_check.py"""
import os
from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
    app_env: str
    openai_api_key: str | None

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            app_env=os.getenv("APP_ENV", "development"),
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )

def main() -> None:
    s = Settings.from_env()
    print("APP_ENV=", s.app_env)
    # Never print the key. Print a boolean.
    print("OPENAI_API_KEY set=", bool(s.openai_api_key))

if __name__ == "__main__":
    main()
''',
            "line_by_line": """- `os.getenv` returns `None` if missing — better than `os.environ[key]` which explodes.
- We print `bool(key)` so logs stay safe.
- `dataclass(frozen=True)` makes settings immutable.""",
            "output": "APP_ENV= development\nOPENAI_API_KEY set= False",
            "dry_run": "Process starts with a copy of the parent environment. `from_env` reads two names. Missing key → None → False.",
            "memory": "Two small strings. Frozen dataclass is one object.",
            "time": "O(1)",
            "space": "O(1)",
            "alternatives": "Pydantic `BaseSettings` (Phase 3) for typed, nested, validated config.",
            "optimization": "Cache settings at startup. Do not read env on every request in a loop (still cheap, but messy).",
        },
    ],
    "practice": [
        {
            "title": "Fifteen-minute terminal gym",
            "body": "Create `~/ai-lab/tmp`, make a file, pipe `echo hello | wc -c`, then `false; echo $?`. Write down the exit code.",
            "done": "`$?` after `false` is 1, and you are not scared.",
        },
        {
            "title": "Venv muscle memory",
            "body": "Create `.venv`, activate, `pip install ruff`, `which python`, deactivate, `which python` again. The path must change.",
            "done": "You can do it without looking at notes.",
        },
        {
            "title": "Git loop",
            "body": "Branch `practice/setup`, commit `sanity.py`, push, open a PR, merge, pull `main`.",
            "done": "GitHub shows the PR.",
        },
    ],
    "exercises": {
        "beginner": [
            {
                "title": "Ignore the right things",
                "body": "Write a `.gitignore` that excludes `.venv/`, `.env`, `__pycache__/`, and `*.pyc` but NOT `.env.example`.",
                "constraints": "No broad `*` that hides Python source.",
            },
            {
                "title": "Sanity script",
                "body": "Extend `sanity.py` to also print whether Docker is reachable (`docker info` via subprocess) without crashing if it is not.",
                "constraints": "Exit 0 even if Docker is down; print a clear message.",
            },
        ],
        "medium": [
            {
                "title": "Makefile or justfile",
                "body": "Add `make setup` that creates venv and installs requirements, and `make sanity` that runs the probe.",
                "constraints": "Works on macOS and Linux. Document Windows equivalent.",
            },
            {
                "title": "Pre-commit",
                "body": "Add `ruff` as a pre-commit hook so bad syntax cannot be committed.",
                "constraints": "Hook runs in under 3 seconds on this repo slice.",
            },
        ],
        "hard": [
            {
                "title": "Devcontainer",
                "body": "Write a `.devcontainer/devcontainer.json` that uses Python 3.12, installs Docker-in-Docker or expects the host Docker socket, and auto-creates a venv.",
                "constraints": "A classmate can Open in Container and run sanity.py.",
            }
        ],
    },
    "assignments": [
        {
            "title": "Onboarding README",
            "time": "90 minutes",
            "brief": "Pretend a new intern starts Monday. Write a README for a fake service that includes OS support, Python version, venv, Docker, and how to run tests. No fluff.",
            "deliverables": ["README.md", "screenshot of sanity.py output", ".env.example"],
            "rubric": [
                "A stranger can follow it without Slack",
                "Secrets are named, not pasted",
                "Windows + macOS + Linux considered",
            ],
        }
    ],
    "quiz": [
        {
            "q": "A command succeeded. Its exit code is:",
            "choices": {"A": "1", "B": "0", "C": "-1", "D": "None"},
            "answer": "B",
            "explain": "Unix convention: 0 success, non-zero failure.",
        },
        {
            "q": "Why use a virtual environment?",
            "choices": {
                "A": "It makes Python faster",
                "B": "It isolates project dependencies",
                "C": "It replaces Docker",
                "D": "It encrypts your code",
            },
            "answer": "B",
            "explain": "Isolation. Speed is unrelated. Docker is a different isolation layer.",
        },
        {
            "q": "Which file SHOULD be committed?",
            "choices": {"A": ".env", "B": ".venv/", "C": ".env.example", "D": "id_rsa"},
            "answer": "C",
            "explain": "Examples of names, never values.",
        },
        {
            "q": "On Windows, where should the Git repo live when using WSL2?",
            "choices": {
                "A": "C:\\\\Users\\\\you\\\\repo",
                "B": "/mnt/c/Users/you/repo",
                "C": "Inside the Linux home, e.g. ~/repo",
                "D": "On a USB stick",
            },
            "answer": "C",
            "explain": "/mnt/c is slow and causes permission weirdness.",
        },
        {
            "q": "What does Docker add that a venv does not?",
            "choices": {
                "A": "Type hints",
                "B": "An isolated OS-level runtime plus system packages",
                "C": "A faster Python",
                "D": "Free GPUs",
            },
            "answer": "B",
            "explain": "venv isolates Python packages. Docker isolates the machine shape.",
        },
        {
            "q": "Port 8000 is already in use. First move?",
            "choices": {
                "A": "Reinstall Python",
                "B": "Find the process bound to 8000 and stop it or pick another port",
                "C": "Disable the firewall",
                "D": "Delete .venv",
            },
            "answer": "B",
            "explain": "One listener per port.",
        },
        {
            "q": "`python` on PATH is 3.9, but `.venv` is 3.12. Which runs after activation?",
            "choices": {"A": "3.9", "B": "3.12", "C": "Both randomly", "D": "Neither"},
            "answer": "B",
            "explain": "Activation prepends `.venv/bin` to PATH.",
        },
        {
            "q": "The safest way to give GitHub your identity from a laptop is:",
            "choices": {
                "A": "Commit your password in .gitconfig",
                "B": "SSH key or gh auth login",
                "C": "Disable HTTPS",
                "D": "Share a teammate's token",
            },
            "answer": "B",
            "explain": "Credential helpers / SSH. Never a password in Git.",
        },
        {
            "q": "CI (GitHub Actions) most commonly runs on:",
            "choices": {"A": "Your laptop OS", "B": "Linux VMs", "C": "iOS", "D": "DOS"},
            "answer": "B",
            "explain": "ubuntu-latest is the default. Test Linux early.",
        },
        {
            "q": "You pasted an API key into a public commit then deleted the file in a new commit. The key is:",
            "choices": {
                "A": "Safe, Git forgets",
                "B": "Still in history and must be rotated",
                "C": "Encrypted automatically",
                "D": "Only visible to you",
            },
            "answer": "B",
            "explain": "History keeps blobs. Rotate the secret. Then rewrite history if needed.",
        },
    ],
    "flashcards": [
        {"q": "Exit code 0 means?", "a": "Success."},
        {"q": "What folder is a venv usually called?", "a": ".venv (or venv)."},
        {"q": "Name two things that must be gitignored.", "a": ".venv and .env (and __pycache__)."},
        {"q": "What is a port?", "a": "A number a process binds so others can talk to it on that machine."},
        {"q": "WSL repos should live where?", "a": "In the Linux filesystem, not under /mnt/c."},
        {"q": "venv vs Docker in one line?", "a": "venv isolates Python packages; Docker isolates the whole runtime."},
        {"q": "What is PATH?", "a": "Directories the shell searches for executables."},
        {"q": "Why lock files?", "a": "Same dependency versions on every machine and in CI."},
        {"q": "What does uv replace for many people?", "a": "pip + venv + pip-tools, faster."},
        {"q": "First thing to check on ModuleNotFoundError?", "a": "Which python (sys.executable) and whether the venv is active."},
    ],
    "interview": [
        {
            "q": "What is a virtual environment and why should I care?",
            "junior": "A directory with its own Python and packages so project A and B can depend on different versions. Without it, global installs collide.",
            "mistakes": "Saying 'it makes Python faster' or mixing it up with Docker / conda without knowing the difference.",
            "senior": "Talk about reproducibility, CI parity, and how lock files + venv beat 'pip install latest' on a laptop that has been alive since 2019.",
        },
        {
            "q": "When do you reach for Docker vs a venv?",
            "junior": "venv for Python libs. Docker when I need system packages, other services, or to match production Linux.",
            "mistakes": "Dockerizing every script. Or never using Docker and shipping 'install Postgres yourself' as a README.",
            "senior": "Devcontainers, multi-stage builds, and the cost of Docker on macOS file mounts. Also: not using Docker as a secrets manager.",
        },
        {
            "q": "A teammate committed an API key. What do you do?",
            "junior": "Rotate the key immediately. Remove it from the repo. Add .env to gitignore. Check Git history.",
            "mistakes": "Only deleting the file in a new commit and considering it solved.",
            "senior": "Incident: rotate, audit usage logs, purge history or treat the repo as compromised, add secret scanning (gitleaks, GitHub scanning), blameless postmortem.",
        },
        {
            "q": "Explain WSL vs dual boot vs a Linux VM.",
            "junior": "WSL2 is a lightweight Linux kernel on Windows. Dual boot is a full OS switch. A VM is heavier isolation.",
            "mistakes": "Claiming WSL is 'just an emulator' (WSL2 is a real kernel) or putting repos on /mnt/c.",
            "senior": "I/O performance, Docker Desktop backend, GPU passthrough limits, corporate policy.",
        },
        {
            "q": "How do you make onboarding a 15-minute task?",
            "junior": "README, .env.example, compose, one setup command, a sanity check.",
            "mistakes": "A 40-page Confluence novel and no compose file.",
            "senior": "Devcontainers or nix, golden images, seed data, a 'hello request' in CI that hits the stack.",
        },
    ],
    "whiteboard": [
        "Draw how a Python process finds a package (PATH, venv, site-packages).",
        "Sketch a laptop → GitHub → Actions → runner path and mark where secrets live.",
        "A Windows teammate is slow in WSL. Diagnose.",
    ],
    "interview_listen": "calm hygiene: venvs, secrets, Linux CI, and no cargo-cult Docker",
    "cheatsheet": {
        "remember": """- 0 = success
- Activate venv before pip
- .env never committed
- Repos in Linux FS on WSL
- Docker daemon must be running""",
        "bash": """python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\\Scripts\\activate
python -m pip install -U pip
pip install -r requirements.txt
uv venv && uv pip install -r requirements.txt
docker compose up --build
echo $?                            # last exit code
ssh-keygen -t ed25519 -C "you@mail"
gh auth login""",
        "python": """import sys
print(sys.executable)
print(sys.prefix != sys.base_prefix)  # in venv?""",
        "decisions": """```mermaid
flowchart TD
  A[Need isolation?] --> B{Python packages only?}
  B -->|yes| C[venv / uv]
  B -->|also OS or other services| D[Docker Compose]
```""",
        "numbers": "- Python 3.11 or 3.12 for this course\n- Common dev ports: 8000 (API), 5432 (Postgres), 6379 (Redis), 6333 (Qdrant)",
        "do_not": "- pip install as root\n- Store keys in source\n- Work in /mnt/c\n- Commit .venv",
    },
    "miniproject": {
        "name": "ai-eng-lab bootstrap",
        "time": "Half a day",
        "difficulty": "Easy",
        "why": "You need a home for every later mini-project. Build it once, properly.",
        "story": "As a future intern, I can clone my lab repo on a new laptop and be running in 15 minutes.",
        "must": [
            "Public GitHub repo with MIT license",
            "README with OS notes, Python version, venv, Docker",
            ".env.example and .gitignore",
            "code/sanity.py that fails if not in a venv",
            "GitHub Actions running sanity.py on ubuntu-latest",
        ],
        "should": ["Makefile or justfile", "ruff config", "VS Code settings example"],
        "wont": ["Kubernetes", "A custom Linux distro", "Zsh ricing"],
        "architecture": """```mermaid
flowchart LR
  Clone --> Venv --> Sanity
  Sanity --> Actions
```""",
        "layout": """ai-eng-lab/
  README.md
  .env.example
  .gitignore
  requirements.txt
  code/sanity.py
  .github/workflows/ci.yml""",
        "rubric": ["Clone works", "CI green", "No secrets", "README under 200 lines"],
        "stretch": "Add a devcontainer.",
    },
    "resources": {
        "official": [
            "[Python 3 docs — venv](https://docs.python.org/3/library/venv.html)",
            "[uv documentation](https://docs.astral.sh/uv/)",
            "[Git SCM book](https://git-scm.com/book/en/v2)",
            "[Docker docs](https://docs.docker.com/)",
            "[VS Code Python](https://code.visualstudio.com/docs/languages/python)",
        ],
        "extra": [
            "[The missing semester of your CS education (MIT)](https://missing.csail.mit.edu/)",
            "[Oh My Git!](https://ohmygit.org/) if Git is still scary",
        ],
        "papers": ["Not a paper phase. Read the Missing Semester notes instead."],
    },
    "faq": [
        {
            "q": "Do I have to use Linux?",
            "a": "No. macOS is excellent. Windows + WSL2 is the supported Windows path. Native Windows without WSL will fight Docker and Unix tutorials.",
        },
        {
            "q": "Conda or venv?",
            "a": "venv/uv for this course. Conda is fine in data-science shops; mixing conda + pip + Docker blindly is how environments rot.",
        },
        {
            "q": "Cursor / Windsurf / Neovim instead of VS Code?",
            "a": "Yes. You still need a terminal, a Python interpreter picker, and Docker. The editor is not the skill.",
        },
        {
            "q": "I don't have admin rights on my laptop.",
            "a": "Use user-level installs, pyenv/uv in home, or a cloud devbox (GitHub Codespaces). Document the constraint.",
        },
        {
            "q": "Is Docker Desktop paid?",
            "a": "Docker Inc. has license rules for large companies. As a student, Docker Desktop or Engine + Compose V2 is fine. Colima or Podman are alternatives on macOS/Linux.",
        },
    ],
    "debugging": [
        {
            "title": "`python` opens the Microsoft Store",
            "symptom": "Windows: typing python tries to install Python from the Store.",
            "wrong": "Python is installed because you installed it once in 2021.",
            "see": "`where python` and App execution aliases in Windows Settings.",
            "fix": "Disable Store aliases. Install Python 3.12. Use `py -3.12`. In WSL, use Linux Python.",
            "prevent": "Develop inside WSL. Document `py -3.12` for teammates stuck on Windows.",
        },
        {
            "title": "ModuleNotFoundError after pip install",
            "symptom": "You installed fastapi but Python cannot import it.",
            "wrong": "pip and python are the same environment.",
            "see": "`python -m pip --version` vs `pip --version` vs `sys.executable`.",
            "fix": "Always `python -m pip install ...` using the venv interpreter.",
            "prevent": "Never use a global pip. `uv run` also prevents this.",
        },
        {
            "title": "Docker: Cannot connect to the Docker daemon",
            "symptom": "CLI works, daemon doesn't.",
            "wrong": "Docker is a single binary. It is a client plus a background engine.",
            "see": "Is Docker Desktop running? `docker info`. On Linux, is your user in the `docker` group?",
            "fix": "Start the engine. Log out/in after adding the group. Never `sudo docker` as a lifestyle.",
            "prevent": "README: 'Start Docker Desktop first.'",
        },
    ],
    "mistakes": [
        {
            "title": "Global package installs",
            "body": "`sudo pip install tensorflow` on the system Python. One month later nothing uninstalls cleanly.",
            "instead": "venv per project. Or uv.",
        },
        {
            "title": "Committing .env because 'it's just a school key'",
            "body": "Bots scrape GitHub for `sk-` prefixes continuously.",
            "instead": ".gitignore + secret scanning. Rotate if leaked.",
        },
        {
            "title": "Spaces in project paths",
            "body": "`~/My Documents/AI Course` will break naive scripts and Docker volume mounts.",
            "instead": "`~/work/ai-engineer`.",
        },
        {
            "title": "Ignoring CI because 'it works locally'",
            "body": "Actions runs Linux. Your Mac hid the bug.",
            "instead": "Green CI is part of the exit ticket.",
        },
    ],
    "prod_tips": {
        "cost": "A leaked key is the expensive bug at this phase. Budget $0 for setup. Budget time for doing it once.",
        "latency": "WSL on /mnt/c can make `pip install` and Git feel like 2012. Move the repo.",
        "reliability": "Pin Python version. Write a sanity command. Run it in CI.",
        "observability": "Even now: print `sys.executable` in failing jobs. Future you will thank you.",
        "scaling": "Dotfiles do not scale a team. A repo with compose + README does.",
        "checklist": [
            "Python version documented",
            ".gitignore includes .venv and .env",
            ".env.example committed",
            "Sanity script in CI",
            "Docker Desktop (or Engine) starts cleanly",
        ],
    },
    "challenge": {
        "title": "Zero-to-green on a classmate's laptop",
        "body": "Sit with someone else (or a cloud VM). Using only your README, get sanity.py green in 20 minutes without touching the machine yourself — you may only speak.",
        "constraints": ["No 'let me take over'", "No undocumented steps"],
        "success": "They run the script. You found the holes in your README.",
    },
    "solutions": [
        {
            "id": "B1 .gitignore",
            "hint": "Put `.env` not `.env*`. The star would hide `.env.example`.",
            "approach": "List: `.venv/`, `.env`, `__pycache__/`, `*.pyc`, `.pytest_cache/`. Commit `.env.example`.",
        },
        {
            "id": "M2 pre-commit",
            "hint": "pre-commit.com, ruff hook, `pre-commit install`.",
            "approach": "Add `.pre-commit-config.yaml` with ruff and ruff-format. Keep excludes small.",
        },
        {
            "id": "Assignment README",
            "hint": "Three commands. One troubleshooting section. No autobiography.",
            "approach": "Copy the style of this course's top README. Short paragraphs. Copy-pasteable blocks.",
        },
    ],
    "code_files": {
        "sanity.py": '''"""Environment probe. Fail if we are not in a virtualenv."""
from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    in_venv = sys.prefix != sys.base_prefix
    print(f"executable={sys.executable}")
    print(f"version={sys.version.split()[0]}")
    print(f"in_venv={in_venv}")
    print(f"cwd={Path.cwd()}")
    if not in_venv:
        raise SystemExit("Activate .venv first (sys.prefix == sys.base_prefix)")


if __name__ == "__main__":
    main()
''',
        "env_check.py": '''"""Read configuration from the environment. Never print secrets."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_env: str
    openai_api_key: str | None

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            app_env=os.getenv("APP_ENV", "development"),
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )


def main() -> None:
    settings = Settings.from_env()
    print("APP_ENV=", settings.app_env)
    print("OPENAI_API_KEY set=", bool(settings.openai_api_key))


if __name__ == "__main__":
    main()
''',
    },
}
