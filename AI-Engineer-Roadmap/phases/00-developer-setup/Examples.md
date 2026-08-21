# Examples — Phase 0: Developer setup

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).

These examples are small on purpose. The skill is *running them in the right environment.*

---

### Example 1. Detect the interpreter (never guess)

Half of 'module not found' bugs are the wrong Python.

```python
"""code/sanity.py — run after activating .venv"""
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

```

**What every interesting line is doing**

- `sys.prefix != sys.base_prefix` is the reliable venv check.
- `SystemExit` with a message sets exit code 1.
- `if __name__ == "__main__"` stops this from running during imports.

**Expected output**

```text
executable=/home/you/repo/.venv/bin/python
version=3.12.x
in_venv=True
cwd=/home/you/repo
```

**Dry run**

Python starts → imports sys → compares prefixes → prints four lines → exits 0. If prefixes match, raises SystemExit, shell shows a non-zero status.

**Memory**

Tiny. A few strings. No leaks. This is a probe, not an app.

**Time complexity:** O(1)  
**Space complexity:** O(1)

**Alternatives**

`uv run python code/sanity.py` runs inside the project's environment without manual activate.

**Optimization**

None needed. Do not wrap this in Docker.

---

### Example 2. Read secrets from the environment, never from source

The first production-shaped habit.

```python
"""code/env_check.py"""
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

```

**What every interesting line is doing**

- `os.getenv` returns `None` if missing — better than `os.environ[key]` which explodes.
- We print `bool(key)` so logs stay safe.
- `dataclass(frozen=True)` makes settings immutable.

**Expected output**

```text
APP_ENV= development
OPENAI_API_KEY set= False
```

**Dry run**

Process starts with a copy of the parent environment. `from_env` reads two names. Missing key → None → False.

**Memory**

Two small strings. Frozen dataclass is one object.

**Time complexity:** O(1)  
**Space complexity:** O(1)

**Alternatives**

Pydantic `BaseSettings` (Phase 3) for typed, nested, validated config.

**Optimization**

Cache settings at startup. Do not read env on every request in a loop (still cheap, but messy).


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
