# Quiz — Phase 1: Python refresh

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

1. await can appear in:
    A) any function
    B) only async functions
    C) only classes
    D) only main
2. Async speeds up:
    A) pure CPU math
    B) waiting on I/O
    C) disk encryption
    D) GIL removal
3. A generator uses:
    A) return only
    B) yield
    C) goto
    D) eval
4. Pydantic is valuable with LLMs because:
    A) it trains models
    B) it validates runtime shapes
    C) it is a vector DB
    D) it removes tokens
5. time.sleep inside async def:
    A) is fine
    B) blocks the event loop
    C) cancels tasks
    D) is a syntax error
6. A decorator is:
    A) a type hint
    B) a function wrapping another
    C) a Docker feature
    D) a token
7. with statement guarantees:
    A) speed
    B) cleanup via __exit__
    C) async
    D) types
8. Exponential backoff + jitter exists to:
    A) look fancy
    B) avoid synchronized retries
    C) increase errors
    D) train models
9. You should usually retry HTTP:
    A) 400
    B) 401
    C) 503
    D) all of them
10. CancelledError should be:
    A) always swallowed
    B) allowed to propagate after cleanup
    C) ignored
    D) printed as success

---

<details>
<summary>Answers (spoiler)</summary>

1. **B** — Syntax rule.
2. **B** — Concurrency for waiting, not parallelism for CPU.
3. **B** — yield pauses.
4. **B** — Contracts.
5. **B** — Use asyncio.sleep.
6. **B** — wrapper.
7. **B** — even on exception.
8. **B** — thundering herd.
9. **C** — transient. 400 is your bug.
10. **B** — cleanup in finally, then let it raise.

</details>
