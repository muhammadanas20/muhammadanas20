# Cheatsheet — Phase 1: Python refresh

Print or pin. This is not a substitute for Theory.md.

## Remember

- await only in async
- time.sleep blocks
- validate JSON
- timeout + bounded retry
- with/async with for cleanup

## Commands / snippets

```bash
ruff check .
ruff format .
pytest -q
```

```python
from collections.abc import AsyncIterator
async def gen() -> AsyncIterator[str]:
    yield "ok"

```

## Decision tree

CPU? → processes. Many sockets? → async. One script? → sync is fine.

## Numbers

Timeouts: 5–60s for models. Retries: 2–4. Backoff base 0.2s. Jitter tens of ms.

## Do not

Bare except. Infinite retry. Logging API keys. json.loads without schema.
