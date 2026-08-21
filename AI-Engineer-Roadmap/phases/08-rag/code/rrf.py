"""Reciprocal Rank Fusion for hybrid search."""
from __future__ import annotations

from collections import defaultdict


def rrf(*ranked_id_lists: list[str], k: int = 60) -> list[str]:
    scores: dict[str, float] = defaultdict(float)
    for lst in ranked_id_lists:
        for rank, doc_id in enumerate(lst, start=1):
            scores[doc_id] += 1.0 / (k + rank)
    return [d for d, _ in sorted(scores.items(), key=lambda x: -x[1])]


if __name__ == "__main__":
    print(rrf(["a", "b", "c"], ["c", "a", "z"]))
