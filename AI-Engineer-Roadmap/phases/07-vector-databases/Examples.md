# Examples — Phase 7: Vector databases

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. In-memory Chroma-shaped API (no extra daemon)

Learn the operations: add, query, filter.

```python
"""code/toy_store.py"""
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
            if where and any(self.meta[i].get(k) != val for k, val in where.items()):
                continue
            s = float((v / (np.linalg.norm(v) + 1e-12)) @ q)
            hits.append(Hit(self.ids[i], s, self.texts[i], self.meta[i]))
        hits.sort(key=lambda h: -h.score)
        return hits[:k]

```

**What every interesting line is doing**

upsert by id, cosine query, metadata AND filter. This is 90% of every vendor SDK.

**Expected output**

```text
Hit list sorted by score.
```

**Dry run**

Insert N vectors. Filter some out. Sort remaining by cosine.

**Memory**

O(N D) like numpy — this toy has no HNSW.

**Time complexity:** O(N D)  
**Space complexity:** O(N D)

**Alternatives**

Chroma, pgvector, Qdrant.

**Optimization**

HNSW when N grows. Payload index for filters.

---

### Example 2. pgvector SQL

You already operate Postgres.

```python
"""code/pgvector.sql -- run inside Postgres with the extension"""
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE chunks (
  id UUID PRIMARY KEY,
  doc_id UUID NOT NULL,
  tenant_id TEXT NOT NULL,
  body TEXT NOT NULL,
  embedding vector(768) NOT NULL
);

CREATE INDEX chunks_hnsw ON chunks USING hnsw (embedding vector_cosine_ops);
CREATE INDEX chunks_tenant ON chunks (tenant_id);

-- query (application binds $1 as vector, $2 as tenant)
-- SELECT id, body, 1 - (embedding <=> $1) AS score
-- FROM chunks
-- WHERE tenant_id = $2
-- ORDER BY embedding <=> $1
-- LIMIT 5;

```

**What every interesting line is doing**

`vector(768)` must match the model. `<=>` is cosine distance in pgvector. Filter on tenant_id **in the same query**.

**Expected output**

```text
Rows of nearest chunks.
```

**Dry run**

Planner uses HNSW + tenant index depending on selectivity.

**Memory**

HNSW in RAM/shared buffers.

**Time complexity:** Sublinear in N with HNSW; still measure with filters.  
**Space complexity:** Vectors + graph.

**Alternatives**

IVFFlat (rebuild-friendly), Qdrant for heavier filter trees.

**Optimization**

Partial indexes per tenant if tenants are huge and few.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
