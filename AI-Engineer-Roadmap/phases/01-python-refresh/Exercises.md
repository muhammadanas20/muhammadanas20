# Exercises — Phase 1: Python refresh

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

### B1. Generator of windows

Yield overlapping chunks of a list (size 3, overlap 1).

**Constraints:** No extra list of all windows if the input is huge — yield.

### B2. TypedDict vs BaseModel

Model a `ChatMessage` both ways. Write when you would pick each.

**Constraints:** Half-page note plus code.

## Medium

### M1. async retry

Port `retry.py` to async with `asyncio.sleep` and exception filtering (only ConnectionError, TimeoutError).

**Constraints:** Preserve type hints.

### M2. contextlib

Write `closing_client()` that yields an httpx.Client and always closes.

**Constraints:** Use `@contextmanager` first, then a class with `__enter__`.

## Hard

### H1. Cancellable stream

An async generator yields numbers 0..999 with 0.05s delay. If the caller cancels after 0.2s, prove the generator stopped (a flag or log).

**Constraints:** Do not swallow CancelledError.

## Submission shape

Each exercise gets a folder:

```text
exercises/phase1/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
