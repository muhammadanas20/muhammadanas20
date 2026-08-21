# Examples — Phase 12: Production AI / LLMOps

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. Exact cache + token budget

Two ops primitives in 40 lines.

```python
"""code/cache_budget.py"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

@dataclass
class Budget:
    used: int = 0
    limit: int = 100_000

    def charge(self, tokens: int) -> None:
        if self.used + tokens > self.limit:
            raise RuntimeError("budget")
        self.used += tokens

cache: dict[str, str] = {}

def key(prompt: str, model: str) -> str:
    return hashlib.sha256(f"{model}:{prompt}".encode()).hexdigest()

def complete(prompt: str, model: str, budget: Budget, call) -> str:
    k = key(prompt, model)
    if k in cache:
        return cache[k]
    text, tokens = call(prompt)
    budget.charge(tokens)
    cache[k] = text
    return text

```

**What every interesting line is doing**

Key includes model. Budget fail-closed. Cache skips charge on hit (you already paid once).

**Expected output**

```text
Second identical call is free and instant.
```

**Dry run**

miss → call → charge → store. hit → return.

**Memory**

O(unique prompts) — use Redis + TTL in prod.

**Time complexity:** O(1) dict  
**Space complexity:** O(n)

**Alternatives**

Redis SET EX. Provider-side prompt caching.

**Optimization**

TTL. Don't cache user-specific data without tenant in key.

---

### Example 2. Router

Not every question needs the strongest model.

```python
"""code/router.py"""
from __future__ import annotations

def route(question: str) -> str:
    q = question.lower()
    if len(q) < 40 or q.startswith(("hi", "hello", "thanks")):
        return "cheap"
    if any(w in q for w in ("legal", "medical", "refund policy")):
        return "strong"
    return "cheap"

if __name__ == "__main__":
    print(route("hi"), route("What is the refund policy for EU customers?"))

```

**What every interesting line is doing**

A toy classifier. Production: a small model or rules + RAG type. Always log the decision.

**Expected output**

```text
cheap strong
```

**Dry run**

Length and keywords pick a bucket.

**Memory**

O(1)

**Time complexity:** O(len(q))  
**Space complexity:** O(1)

**Alternatives**

Embedding similarity to examples; dedicated classifier.

**Optimization**

Don't call a huge router model that costs more than the savings.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
