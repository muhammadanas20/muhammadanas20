"""Tiny cosine demo."""
from __future__ import annotations

import math


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b, strict=True))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb + 1e-12)


if __name__ == "__main__":
    print(round(cosine([1.0, 0.0], [1.0, 0.0]), 3))
    print(round(cosine([1.0, 0.0], [0.0, 1.0]), 3))
