# Examples — Phase 1: Python refresh

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. Pydantic as a contract for model output

LLMs emit strings. Your app needs objects.

```python
"""code/ticket.py"""
from pydantic import BaseModel, Field, ValidationError

class Ticket(BaseModel):
    # Field descriptions also help structured-output prompts later
    category: str = Field(pattern=r"^(billing|tech|other)$")
    priority: int = Field(ge=1, le=3)
    summary: str = Field(min_length=5, max_length=200)

raw = '{"category":"billing","priority":1,"summary":"Invoice double charge"}'
ticket = Ticket.model_validate_json(raw)
print(ticket.category, ticket.priority)

try:
    Ticket.model_validate_json('{"category":"banana","priority":9,"summary":"x"}')
except ValidationError as exc:
    print("rejected", exc.error_count())

```

**What every interesting line is doing**

`model_validate_json` parses and validates. Invalid category or priority raises. You *never* trust the model blindly.

**Expected output**

```text
billing 1
rejected 3
```

**Dry run**

JSON string → bytes parse → field constraints → Ticket instance. Second call fails on pattern, range, and min_length.

**Memory**

One model instance; ValidationError holds error list.

**Time complexity:** O(n) in JSON size  
**Space complexity:** O(n)

**Alternatives**

json + hand checks; msgspec (faster); attrs + converters.

**Optimization**

Reuse the model class. Do not dynamically create models per request.

---

### Example 2. Retry with timeout — the production primitive

Model APIs flake. Your code must not.

```python
"""code/retry.py"""
from __future__ import annotations

import random
import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")

def retry(times: int = 3, base: float = 0.2) -> Callable[[Callable[..., T]], Callable[..., T]]:
    def deco(fn: Callable[..., T]) -> Callable[..., T]:
        def wrapped(*args: object, **kwargs: object) -> T:
            last: Exception | None = None
            for attempt in range(times):
                try:
                    return fn(*args, **kwargs)
                except Exception as exc:  # in production: catch *transient* only
                    last = exc
                    sleep = base * (2 ** attempt) + random.random() * 0.05
                    time.sleep(sleep)
            assert last is not None
            raise last
        return wrapped
    return deco

@retry(times=3)
def flaky() -> str:
    if random.random() < 0.7:
        raise ConnectionError("nope")
    return "ok"

```

**What every interesting line is doing**

Decorator factory → wrapper loops → exponential backoff + jitter so many clients do not retry in lockstep (thundering herd).

**Expected output**

```text
Sometimes 'ok', sometimes a raised ConnectionError after 3 tries.
```

**Dry run**

attempt 0 fail → sleep ~0.2s → attempt 1 fail → sleep ~0.4s → attempt 2 maybe success.

**Memory**

O(1) besides exception objects.

**Time complexity:** O(times) calls; wall clock is the sleeps  
**Space complexity:** O(1)

**Alternatives**

tenacity library; httpx built-in transports; asyncio.sleep in async version.

**Optimization**

Cap sleep. Add retry-after header support. Do not retry HTTP 400.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
