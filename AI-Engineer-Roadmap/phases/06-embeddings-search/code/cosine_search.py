"""Brute-force cosine search — the whole idea of a vector DB."""
from __future__ import annotations

import numpy as np


def normalize(x: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(x, axis=1, keepdims=True) + 1e-12
    return x / n


def search(index: np.ndarray, query: np.ndarray, k: int = 3) -> tuple[np.ndarray, np.ndarray]:
    idx_n = normalize(index)
    q_n = query / (np.linalg.norm(query) + 1e-12)
    scores = idx_n @ q_n
    k = min(k, scores.shape[0])
    top = np.argpartition(-scores, kth=k - 1)[:k]
    order = top[np.argsort(-scores[top])]
    return order, scores[order]


if __name__ == "__main__":
    rng = np.random.default_rng(0)
    index = rng.normal(size=(100, 8))
    query = index[42] + 0.01 * rng.normal(size=(8,))
    ids, sc = search(index, query, k=3)
    print(list(ids), sc.round(3))
