"""Environment probe. Fail if we are not in a virtualenv."""
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
