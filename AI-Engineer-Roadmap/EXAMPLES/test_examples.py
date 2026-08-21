"""Tiny tests so CI has a real pytest target."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from cosine import cosine  # noqa: E402
from rrf import rrf  # noqa: E402


def test_cosine_identical() -> None:
    assert cosine([1.0, 0.0], [1.0, 0.0]) == 1.0


def test_rrf_prefers_overlap() -> None:
    fused = rrf(["a", "b"], ["a", "c"])
    assert fused[0] == "a"
