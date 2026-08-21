#!/usr/bin/env python3
"""Render all phase lesson files from scripts/phases/pXX.py modules."""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from render import write_phase  # noqa: E402

SLUGS = [
    ("00-developer-setup", "p00"),
    ("01-python-refresh", "p01"),
    ("02-sql-databases", "p02"),
    ("03-fastapi", "p03"),
    ("04-docker", "p04"),
    ("05-llm-fundamentals", "p05"),
    ("06-embeddings-search", "p06"),
    ("07-vector-databases", "p07"),
    ("08-rag", "p08"),
    ("09-agents", "p09"),
    ("10-mcp", "p10"),
    ("11-deployment", "p11"),
    ("12-production-ai", "p12"),
    ("13-security", "p13"),
    ("14-capstone", "p14"),
]


def main() -> None:
    for slug, modname in SLUGS:
        try:
            mod = importlib.import_module(f"phases.{modname}")
        except ModuleNotFoundError:
            print(f"SKIP missing {modname}")
            continue
        write_phase(ROOT, slug, mod.PHASE)
        print(f"wrote phases/{slug}")


if __name__ == "__main__":
    main()
