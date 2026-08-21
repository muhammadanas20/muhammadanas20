"""Minimal vector store API: upsert, cosine query, metadata filter."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class Hit:
    id: str
    score: float
    text: str
    meta: dict


class ToyStore:
    def __init__(self, dim: int) -> None:
        self.dim = dim
        self.ids: list[str] = []
        self.vecs: list[np.ndarray] = []
        self.texts: list[str] = []
        self.meta: list[dict] = []

    def upsert(self, id: str, vec: np.ndarray, text: str, meta: dict | None = None) -> None:
        assert vec.shape == (self.dim,)
        if id in self.ids:
            i = self.ids.index(id)
            self.vecs[i], self.texts[i], self.meta[i] = vec, text, meta or {}
            return
        self.ids.append(id)
        self.vecs.append(vec)
        self.texts.append(text)
        self.meta.append(meta or {})

    def query(self, vec: np.ndarray, k: int = 3, where: dict | None = None) -> list[Hit]:
        hits: list[Hit] = []
        q = vec / (np.linalg.norm(vec) + 1e-12)
        for i, v in enumerate(self.vecs):
            if where and any(self.meta[i].get(key) != val for key, val in where.items()):
                continue
            s = float((v / (np.linalg.norm(v) + 1e-12)) @ q)
            hits.append(Hit(self.ids[i], s, self.texts[i], self.meta[i]))
        hits.sort(key=lambda h: -h.score)
        return hits[:k]
