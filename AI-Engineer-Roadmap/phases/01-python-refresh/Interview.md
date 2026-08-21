# Interview — Phase 1: Python refresh

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. When would you not use asyncio?

**Expected answer (junior)**

CPU-heavy work, simple scripts, or when the library is blocking and tiny QPS does not justify a thread pool.

**Common mistakes**

Async everything. Or 'async makes code faster' without saying I/O.

**Senior-level discussion**

 GIL, uvloop, running sync SDK in `asyncio.to_thread`, backpressure, and why two event loops in one process is a footgun.
### Q2. How do you type LLM output?

**Expected answer (junior)**

Pydantic model, validate JSON, reject on error, maybe retry with the validation error as feedback.

**Common mistakes**

Index into a dict of dicts and hope.

**Senior-level discussion**

JSON schema / constrained decoding, repair loops with a cap, logging the raw payload to traces not stdout.
### Q3. Explain a decorator to a beginner, then to a senior.

**Expected answer (junior)**

A wrapper that adds behavior. @retry.

**Common mistakes**

Confusing decorators with subclasses or with FastAPI dependencies.

**Senior-level discussion**

functools.wraps, parametrized decorators, stacking order, async-aware wrappers, cost of extra stack frames.
### Q4. A streaming response must stop when the client disconnects. How?

**Expected answer (junior)**

Catch disconnect, cancel the upstream request, use finally to close.

**Common mistakes**

Ignoring cancellation; buffering the whole answer.

**Senior-level discussion**

Starlette Request.is_disconnected, httpx ACL, paying for tokens you no longer stream, tracing the cancel.
### Q5. What is exponential backoff?

**Expected answer (junior)**

Wait 0.2, 0.4, 0.8... after failures so you do not hammer a sick service.

**Common mistakes**

Retry instantly in a hot loop. Retry 400s.

**Senior-level discussion**

Jitter, retry-after, circuit breakers, idempotency keys, distinguishing 429 vs 500.


---

## Whiteboard prompts

- Draw the event loop for two concurrent chat requests sharing one httpx.AsyncClient.
- Sketch retry + timeout around a model call. Mark what is retried.
- Convert a sync for-loop that builds a giant string of tokens into a generator. Discuss memory.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for whether you treat Python as a production language: types, timeouts, cancellation.
