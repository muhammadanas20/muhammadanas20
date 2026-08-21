"""Reciprocal rank fusion."""
from collections import defaultdict


def rrf(*lists: list[str], k: int = 60) -> list[str]:
    scores: dict[str, float] = defaultdict(float)
    for lst in lists:
        for rank, doc_id in enumerate(lst, start=1):
            scores[doc_id] += 1.0 / (k + rank)
    return [d for d, _ in sorted(scores.items(), key=lambda x: -x[1])]


if __name__ == "__main__":
    print(rrf(["a", "b", "c"], ["c", "a", "z"]))
