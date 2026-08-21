# Examples — Phase 6: Embeddings and search

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. Cosine search in pure numpy

If you cannot do this, a vector DB is a black box.

```python
"""code/cosine_search.py"""
from __future__ import annotations

import numpy as np

def normalize(x: np.ndarray) -> np.ndarray:
    n = np.linalg.norm(x, axis=1, keepdims=True) + 1e-12
    return x / n

def search(index: np.ndarray, query: np.ndarray, k: int = 3) -> tuple[np.ndarray, np.ndarray]:
    """index (N, D), query (D,) both unnormalized. Returns (indices, scores)."""
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
    print(ids, sc.round(3))

```

**What every interesting line is doing**

Normalize rows to unit length. Dot product = cosine. argpartition is O(N) for top-k, faster than full sort.

**Expected output**

```text
[42 ...] with the first score ~1.0
```

**Dry run**

Build random index. Query near row 42. Cosine peak at 42.

**Memory**

O(N*D) for the matrix. 10k * 768 * 4 bytes ≈ 30MB.

**Time complexity:** O(N D) brute force  
**Space complexity:** O(N D)

**Alternatives**

faiss, hnswlib, a vector DB.

**Optimization**

ANN when N is large. Filter metadata first if selective.

---

### Example 2. Heading-aware chunker (Markdown)

Naive windows murder documentation.

```python
"""code/chunk_md.py"""
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Chunk:
    heading: str
    text: str

def chunk_markdown(md: str, max_chars: int = 800) -> list[Chunk]:
    chunks: list[Chunk] = []
    heading = "root"
    buf: list[str] = []

    def flush() -> None:
        text = "\n".join(buf).strip()
        if text:
            chunks.append(Chunk(heading=heading, text=text))
        buf.clear()

    for line in md.splitlines():
        if line.startswith("#"):
            flush()
            heading = line.lstrip("#").strip() or heading
            continue
        buf.append(line)
        if sum(len(x) for x in buf) >= max_chars:
            flush()
    flush()
    return chunks

```

**What every interesting line is doing**

Split on headings first. Only then apply a size cap. Each chunk keeps the heading as metadata for citations.

**Expected output**

```text
A list of Chunk(heading=..., text=...)
```

**Dry run**

See a # line → flush previous buffer, start new heading.

**Memory**

O(document)

**Time complexity:** O(n) characters  
**Space complexity:** O(n)

**Alternatives**

RecursiveCharacterTextSplitter; HTML header splits; PDF by pages (worse) vs by layout (better).

**Optimization**

Token-length not chars. Keep overlap of last 1–2 sentences.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
