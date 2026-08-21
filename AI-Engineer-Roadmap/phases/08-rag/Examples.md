# Examples — Phase 8: Retrieval-Augmented Generation (RAG)

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. Naive RAG in one file (fake retrieve + generate)

See the data flow without 12 libraries.

```python
"""code/naive_rag.py"""
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Hit:
    id: str
    text: str
    score: float

CORPUS = [
    Hit("h1", "A token is a piece of text the model bills and counts.", 0),
    Hit("h2", "Docker images are immutable snapshots.", 0),
    Hit("h3", "Redis is great for rate limits, not chat history.", 0),
]

def retrieve(q: str, k: int = 2) -> list[Hit]:
    ql = q.lower().split()
    scored: list[Hit] = []
    for h in CORPUS:
        score = sum(w in h.text.lower() for w in ql)
        scored.append(Hit(h.id, h.text, float(score)))
    scored.sort(key=lambda x: -x.score)
    return scored[:k]

def prompt(q: str, hits: list[Hit]) -> str:
    src = "\n".join(f"[{h.id}] {h.text}" for h in hits)
    return (
        "Use ONLY the sources. If missing, say you don't know.\n"
        f"Sources:\n{src}\n\nQuestion: {q}\nAnswer:"
    )

def generate_fake(p: str) -> str:
    if "h1" in p and "token" in p.lower():
        return "A token is a billed text piece [h1]."
    return "I don't know."

if __name__ == "__main__":
    q = "What is a token?"
    hits = retrieve(q)
    print(generate_fake(prompt(q, hits)))

```

**What every interesting line is doing**

retrieve is testable. prompt is a pure function. generate is replaceable with a real model. Fake keyword retrieve stands in for vectors.

**Expected output**

```text
A token is a billed text piece [h1].
```

**Dry run**

Query → score corpus by word overlap → top 2 → prompt → fake generate sees h1.

**Memory**

O(corpus)

**Time complexity:** O(|corpus| * |query|)  
**Space complexity:** O(k)

**Alternatives**

Replace retrieve with cosine / hybrid.

**Optimization**

This is the skeleton. Don't add GraphRAG here.

---

### Example 2. RRF fusion of two ranked lists

Hybrid search without learned weights.

```python
"""code/rrf.py"""
from __future__ import annotations

from collections import defaultdict

def rrf(*ranked_id_lists: list[str], k: int = 60) -> list[str]:
    """Reciprocal Rank Fusion. k=60 is the common constant, not top-k."""
    scores: dict[str, float] = defaultdict(float)
    for lst in ranked_id_lists:
        for rank, doc_id in enumerate(lst, start=1):
            scores[doc_id] += 1.0 / (k + rank)
    return [d for d, _ in sorted(scores.items(), key=lambda x: -x[1])]

if __name__ == "__main__":
    dense = ["a", "b", "c"]
    bm25 = ["c", "a", "z"]
    print(rrf(dense, bm25))

```

**What every interesting line is doing**

Each list contributes 1/(k+rank). Docs that rank well in both win. No score calibration needed.

**Expected output**

```text
['a', 'c', 'b', 'z'] or similar — a and c boosted.
```

**Dry run**

a: 1/61 + 1/62; c: 1/63 + 1/61 — compute and sort.

**Memory**

O(n) unique ids

**Time complexity:** O(n log n) sort  
**Space complexity:** O(n)

**Alternatives**

Weighted sum of min-max normalized scores; learned fusion.

**Optimization**

RRF is the default until eval says otherwise.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
