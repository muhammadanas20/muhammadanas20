"""Exact cache + token budget."""
from __future__ import annotations

import hashlib
from dataclasses import dataclass


@dataclass
class Budget:
    used: int = 0
    limit: int = 100_000

    def charge(self, tokens: int) -> None:
        if self.used + tokens > self.limit:
            raise RuntimeError("budget")
        self.used += tokens


def key(prompt: str, model: str) -> str:
    return hashlib.sha256(f"{model}:{prompt}".encode()).hexdigest()
