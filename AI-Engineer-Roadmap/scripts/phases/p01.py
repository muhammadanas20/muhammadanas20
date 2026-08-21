PHASE = {
    "num": "1",
    "title": "Python refresh",
    "tagline": "The Python that AI services actually use: types, async, generators, decorators, context managers.",
    "hours": "5-7 days",
    "difficulty": "Easy",
    "exit_ticket": "A typed async HTTP client with retries, timeouts, and a context-managed session.",
    "objectives": [
        "Write type-annotated Python 3.11 that pydantic and your teammates can trust.",
        "Explain the event loop and when async helps (I/O) vs hurts (CPU).",
        "Stream data with generators and `async for`.",
        "Write decorators for timing, retry, and auth.",
        "Use context managers so clients and files always close.",
    ],
    "prerequisites": [
        "Phase 0 complete.",
        "You can write a class, a function, and a list comprehension.",
        "You have used NumPy/Pandas at least once (we will not reteach DataFrames).",
    ],
    "topics": ["Typing", "Pydantic", "Async/await", "Generators", "Decorators", "Context managers", "Retries"],
    "nav": "[Home](../../README.md) · Prev: [Phase 0](../00-developer-setup/) · Next: [Phase 2 · SQL](../02-sql-databases/)",
    "theory": {
        "intro": """AI engineering is mostly **waiting on networks**: model APIs, databases, vector stores, browsers.

The Python that matters is therefore:

- **Types** so a model's JSON cannot silently become the wrong shape
- **Async** so one process can wait on many sockets
- **Generators** so you can stream tokens without building a giant string
- **Decorators** so retries and tracing are not copy-pasted
- **Context managers** so HTTP sessions and file handles close even when the model throws

This is not a beginner Python course. It is the subset that shows up in every production LLM service.""",
        "one_liner": "Typed async Python is the language of AI backends.",
        "why": """Without types, `response['choices'][0]['message']['content']` explodes at 2am.

Without async, your FastAPI server handles one streaming chat at a time.

Without generators, you buffer a 4,000-token answer before sending a byte.

Without retries and timeouts, a 15-second model blip becomes a hung worker.

These are not style points. They are the difference between a notebook and a service.""",
        "if_missing": "you would paste `time.sleep` in request handlers and parse LLM JSON with hope.",
        "analogy": """A restaurant.

- **Types / Pydantic** = the ticket the kitchen accepts. If "table 4 wants pasta" is missing a table number, you reject it *before* cooking.
- **Async** = one waiter taking drink orders from many tables while the espresso machine works. The waiter is not faster at pouring. They just do not freeze the whole room while the machine hisses.
- **Generators** = plating bite by bite instead of cooking the entire banquet before serving.
- **Decorators** = a standard "check allergy card" step wrapped around any dish.
- **Context managers** = unlocking the pantry and *always* locking it, even if the sauce catches fire.""",
        "visual": """```mermaid
sequenceDiagram
  participant C as Caller
  participant L as Event loop
  participant H as HTTP to model
  participant D as Database
  C->>L: await chat()
  L->>H: send prompt (non-blocking)
  L->>D: fetch user (while waiting)
  H-->>L: token chunk
  L-->>C: yield chunk
```""",
        "architecture": """```mermaid
flowchart TB
  subgraph request [One chat request]
    V[Pydantic validate in]
    A[async handler]
    G[async generator stream]
    T[timeout + retry decorator]
    CM[httpx.AsyncClient context]
  end
  V --> A --> T --> CM --> G
```""",
        "beginner": """**Type hints** are notes about what a value should be. `def f(x: int) -> str` means x is an int and f returns a string. Python does not enforce this at runtime unless you use a tool (mypy, pyright) or pydantic.

**Pydantic** is a library that *does* enforce shapes at runtime. Perfect for LLM JSON.

**`async def`** defines a coroutine. Calling it does not run it. `await` does. You can only `await` inside async functions.

**Event loop** = the scheduler that runs coroutines when their I/O is ready.

**Generator** = a function with `yield`. It pauses and resumes. Great for streams.

**Decorator** = a function that takes a function and returns a wrapped one. `@retry` is a decorator.

**Context manager** = an object that works with `with`. `__enter__` / `__exit__` (or `async with`). Guarantees cleanup.""",
        "intermediate": """**`from __future__ import annotations`** delays evaluation of hints so you can reference types before they exist.

**`TypeAlias`, `TypedDict`, `Protocol`** model shapes without full classes. Protocols are like interfaces.

**`asyncio.gather`** runs several coroutines concurrently. **`TaskGroup`** (3.11+) is the safer structured version.

**CPU-bound work** (embedding a huge file in pure Python) does **not** get faster with async. Use a process pool or a different language/library. Async is for waiting.

**`yield from` and `async for`** compose streams.

**Decorator factories** (`def retry(times): def deco(fn): ...`) take parameters.

**`contextlib.contextmanager`** lets you write a context manager as a generator with one `yield`.""",
        "advanced": """**Backpressure.** If you yield tokens faster than the client reads, you buffer. `asyncio.Queue(maxsize=...)` and Starlette streaming responses matter.

**Cancellation.** When a user closes a tab, you must cancel the model HTTP call or you pay for unused tokens. `try/finally` and `httpx` timeouts.

**Re-entrancy.** A naive decorator that locks a global will deadlock under async.

**Type narrowing.** `assert x is not None` after a check so pyright is happy.

**Pydantic v2** is a different beast from v1 (`model_validate`, `model_dump`). Use v2.

**`slots` / frozen dataclasses** for hot path objects (chunks, spans).""",
        "production": """In production AI services:

- All external calls have **timeouts**.
- Retries are **bounded** and **idempotent** (do not retry a non-idempotent POST without care).
- Streams are **async generators** from the DB to the socket.
- Settings are typed.
- You log **request ids**, not prompts with PII.

A staff engineer reading your code looks for `timeout=` before they look for clever prompts.""",
        "when": "Every backend. Every client. Every time you talk to a model or a database.",
        "when_not": "Do not make a 20-line script async. Do not type every local variable. Do not retry `POST /charges` blindly.",
        "code_preview": '''import asyncio
from collections.abc import AsyncIterator

async def tokens() -> AsyncIterator[str]:
    for part in ["Hello", " ", "world"]:
        await asyncio.sleep(0.01)  # fake network
        yield part
''',
        "code_notes": "This is the skeleton of LLM streaming. FastAPI will iterate it and send Server-Sent Events.",
        "ex_b": "Annotate a function, write a pydantic model, write a generator that yields lines of a file.",
        "ex_m": "Retry decorator with exponential backoff + jitter. Async version too.",
        "ex_h": "Async client that streams a fake model, can be cancelled, and times out at 2 seconds.",
        "project": "Typed async HTTP client — MiniProject.md.",
        "interview_preview": "When is async useless? What does await do? How does a generator differ from returning a list?",
        "flash_sample": "**Q:** Can you `await` in a sync function?\n**A:** No. SyntaxError / design error.",
        "mistakes_preview": "`time.sleep` in async code. Bare `except:`. Retrying without timeout. `json.loads` on LLM output without a schema.",
        "debug_preview": "`RuntimeWarning: coroutine was never awaited`. Deadlocks from `time.sleep`. CancelledError swallowed.",
        "best": "- Type public functions.\n- Timeout every awaitable I/O.\n- Retry only transient errors (429, 502, 503).\n- Prefer `async with` for clients.\n- Validate all untrusted JSON with pydantic.",
        "industry": "FastAPI + pydantic v2 + httpx + tenacity (or custom retry) is the 2024–2026 default stack for Python AI services.",
        "perf": "Avoid extra copies of big strings. Stream. Do not embed files on the event loop. Use `orjson` if JSON encode is hot (measure first).",
        "security": "Do not log full prompts. Do not retry requests that might have side effects without idempotency keys. Timeouts are a security control against slowloris-style hangs.",
        "refs": "- [PEP 484 / 695 typing](https://peps.python.org/pep-0484/)\n- [Pydantic](https://docs.pydantic.dev/)\n- [asyncio](https://docs.python.org/3/library/asyncio.html)\n- [httpx](https://www.python-httpx.org/)",
        "further": "- *Fluent Python* (Ramalho) chapters on coroutines and decorators\n- Any httpx timeout write-up",
    },
    "examples": [
        {
            "title": "Pydantic as a contract for model output",
            "why": "LLMs emit strings. Your app needs objects.",
            "code": '''"""code/ticket.py"""
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
''',
            "line_by_line": "`model_validate_json` parses and validates. Invalid category or priority raises. You *never* trust the model blindly.",
            "output": "billing 1\nrejected 3",
            "dry_run": "JSON string → bytes parse → field constraints → Ticket instance. Second call fails on pattern, range, and min_length.",
            "memory": "One model instance; ValidationError holds error list.",
            "time": "O(n) in JSON size",
            "space": "O(n)",
            "alternatives": "json + hand checks; msgspec (faster); attrs + converters.",
            "optimization": "Reuse the model class. Do not dynamically create models per request.",
        },
        {
            "title": "Retry with timeout — the production primitive",
            "why": "Model APIs flake. Your code must not.",
            "code": '''"""code/retry.py"""
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
''',
            "line_by_line": "Decorator factory → wrapper loops → exponential backoff + jitter so many clients do not retry in lockstep (thundering herd).",
            "output": "Sometimes 'ok', sometimes a raised ConnectionError after 3 tries.",
            "dry_run": "attempt 0 fail → sleep ~0.2s → attempt 1 fail → sleep ~0.4s → attempt 2 maybe success.",
            "memory": "O(1) besides exception objects.",
            "time": "O(times) calls; wall clock is the sleeps",
            "space": "O(1)",
            "alternatives": "tenacity library; httpx built-in transports; asyncio.sleep in async version.",
            "optimization": "Cap sleep. Add retry-after header support. Do not retry HTTP 400.",
        },
    ],
    "practice": [
        {"title": "Type this function", "body": "Take an untyped function from an old notebook. Add hints until pyright is quiet.", "done": "No `Any` unless you can justify it."},
        {"title": "Sleep is not async", "body": "Write two versions of a 1-second fake I/O burst of 10 calls: sync `time.sleep` vs `asyncio.gather` + `asyncio.sleep`. Time both.", "done": "You can explain why gather is ~1s and sync is ~10s."},
        {"title": "with-statement", "body": "Write a context manager that times a block and prints milliseconds.", "done": "Works with exceptions inside the block."},
    ],
    "exercises": {
        "beginner": [
            {"title": "Generator of windows", "body": "Yield overlapping chunks of a list (size 3, overlap 1).", "constraints": "No extra list of all windows if the input is huge — yield."},
            {"title": "TypedDict vs BaseModel", "body": "Model a `ChatMessage` both ways. Write when you would pick each.", "constraints": "Half-page note plus code."},
        ],
        "medium": [
            {"title": "async retry", "body": "Port `retry.py` to async with `asyncio.sleep` and exception filtering (only ConnectionError, TimeoutError).", "constraints": "Preserve type hints."},
            {"title": "contextlib", "body": "Write `closing_client()` that yields an httpx.Client and always closes.", "constraints": "Use `@contextmanager` first, then a class with `__enter__`."},
        ],
        "hard": [
            {"title": "Cancellable stream", "body": "An async generator yields numbers 0..999 with 0.05s delay. If the caller cancels after 0.2s, prove the generator stopped (a flag or log).", "constraints": "Do not swallow CancelledError."},
        ],
    },
    "assignments": [
        {
            "title": "Typed async client",
            "time": "3–4 hours",
            "brief": "Build a small client for https://httpbin.org (or a local FastAPI stub) with timeout, retry, pydantic-parsed JSON, and a streaming endpoint mocked with chunked data.",
            "deliverables": ["package with py.typed", "tests", "README with a timing table"],
            "rubric": ["mypy/pyright clean", "tests for timeout", "no printed secrets"],
        }
    ],
    "quiz": [
        {"q": "await can appear in:", "choices": {"A": "any function", "B": "only async functions", "C": "only classes", "D": "only main"}, "answer": "B", "explain": "Syntax rule."},
        {"q": "Async speeds up:", "choices": {"A": "pure CPU math", "B": "waiting on I/O", "C": "disk encryption", "D": "GIL removal"}, "answer": "B", "explain": "Concurrency for waiting, not parallelism for CPU."},
        {"q": "A generator uses:", "choices": {"A": "return only", "B": "yield", "C": "goto", "D": "eval"}, "answer": "B", "explain": "yield pauses."},
        {"q": "Pydantic is valuable with LLMs because:", "choices": {"A": "it trains models", "B": "it validates runtime shapes", "C": "it is a vector DB", "D": "it removes tokens"}, "answer": "B", "explain": "Contracts."},
        {"q": "time.sleep inside async def:", "choices": {"A": "is fine", "B": "blocks the event loop", "C": "cancels tasks", "D": "is a syntax error"}, "answer": "B", "explain": "Use asyncio.sleep."},
        {"q": "A decorator is:", "choices": {"A": "a type hint", "B": "a function wrapping another", "C": "a Docker feature", "D": "a token"}, "answer": "B", "explain": "wrapper."},
        {"q": "with statement guarantees:", "choices": {"A": "speed", "B": "cleanup via __exit__", "C": "async", "D": "types"}, "answer": "B", "explain": "even on exception."},
        {"q": "Exponential backoff + jitter exists to:", "choices": {"A": "look fancy", "B": "avoid synchronized retries", "C": "increase errors", "D": "train models"}, "answer": "B", "explain": "thundering herd."},
        {"q": "You should usually retry HTTP:", "choices": {"A": "400", "B": "401", "C": "503", "D": "all of them"}, "answer": "C", "explain": "transient. 400 is your bug."},
        {"q": "CancelledError should be:", "choices": {"A": "always swallowed", "B": "allowed to propagate after cleanup", "C": "ignored", "D": "printed as success"}, "answer": "B", "explain": "cleanup in finally, then let it raise."},
    ],
    "flashcards": [
        {"q": "What does await do?", "a": "Pauses the coroutine until the awaitable finishes, letting the loop run other work."},
        {"q": "When is async the wrong tool?", "a": "CPU-bound work; tiny scripts; libraries that are sync-only without a thread."},
        {"q": "Why pydantic over json.loads?", "a": "Types, constraints, useful errors."},
        {"q": "What is jitter in retries?", "a": "Random extra delay so clients desynchronize."},
        {"q": "sync vs async sleep?", "a": "time.sleep blocks the thread/loop; asyncio.sleep yields."},
        {"q": "Protocol vs ABC?", "a": "Protocol is structural typing (has the methods); ABC is nominal inheritance."},
        {"q": "What is an async generator?", "a": "async def with yield; iterate with async for."},
        {"q": "Why frozen dataclass for settings?", "a": "Immutability, fewer accidental writes."},
        {"q": "What is structured concurrency?", "a": "TaskGroup/nursery: child tasks finish or cancel together."},
        {"q": "Name a transient HTTP code.", "a": "429, 502, 503, 504."},
    ],
    "interview": [
        {
            "q": "When would you not use asyncio?",
            "junior": "CPU-heavy work, simple scripts, or when the library is blocking and tiny QPS does not justify a thread pool.",
            "mistakes": "Async everything. Or 'async makes code faster' without saying I/O.",
            "senior": " GIL, uvloop, running sync SDK in `asyncio.to_thread`, backpressure, and why two event loops in one process is a footgun.",
        },
        {
            "q": "How do you type LLM output?",
            "junior": "Pydantic model, validate JSON, reject on error, maybe retry with the validation error as feedback.",
            "mistakes": "Index into a dict of dicts and hope.",
            "senior": "JSON schema / constrained decoding, repair loops with a cap, logging the raw payload to traces not stdout.",
        },
        {
            "q": "Explain a decorator to a beginner, then to a senior.",
            "junior": "A wrapper that adds behavior. @retry.",
            "mistakes": "Confusing decorators with subclasses or with FastAPI dependencies.",
            "senior": "functools.wraps, parametrized decorators, stacking order, async-aware wrappers, cost of extra stack frames.",
        },
        {
            "q": "A streaming response must stop when the client disconnects. How?",
            "junior": "Catch disconnect, cancel the upstream request, use finally to close.",
            "mistakes": "Ignoring cancellation; buffering the whole answer.",
            "senior": "Starlette Request.is_disconnected, httpx ACL, paying for tokens you no longer stream, tracing the cancel.",
        },
        {
            "q": "What is exponential backoff?",
            "junior": "Wait 0.2, 0.4, 0.8... after failures so you do not hammer a sick service.",
            "mistakes": "Retry instantly in a hot loop. Retry 400s.",
            "senior": "Jitter, retry-after, circuit breakers, idempotency keys, distinguishing 429 vs 500.",
        },
    ],
    "whiteboard": [
        "Draw the event loop for two concurrent chat requests sharing one httpx.AsyncClient.",
        "Sketch retry + timeout around a model call. Mark what is retried.",
        "Convert a sync for-loop that builds a giant string of tokens into a generator. Discuss memory.",
    ],
    "interview_listen": "whether you treat Python as a production language: types, timeouts, cancellation",
    "cheatsheet": {
        "remember": "- await only in async\n- time.sleep blocks\n- validate JSON\n- timeout + bounded retry\n- with/async with for cleanup",
        "bash": "ruff check .\nruff format .\npytest -q",
        "python": '''from collections.abc import AsyncIterator
async def gen() -> AsyncIterator[str]:
    yield "ok"
''',
        "decisions": "CPU? → processes. Many sockets? → async. One script? → sync is fine.",
        "numbers": "Timeouts: 5–60s for models. Retries: 2–4. Backoff base 0.2s. Jitter tens of ms.",
        "do_not": "Bare except. Infinite retry. Logging API keys. json.loads without schema.",
    },
    "miniproject": {
        "name": "httpx-mini client",
        "time": "Half a day to one day",
        "difficulty": "Easy-medium",
        "why": "You will wrap OpenAI/Anthropic/Ollama the same way.",
        "story": "As a developer, I can GET/POST JSON with retries and parse into pydantic models.",
        "must": ["Typed public API", "Timeouts", "Retries with jitter", "Tests with respx or httpx MockTransport", "README"],
        "should": ["Async and sync versions", "Stream lines"],
        "wont": ["Full OpenAI clone", "A web UI"],
        "architecture": "```mermaid\nflowchart LR\n  App --> Client --> Retry --> httpx --> Net\n  Client --> Pydantic\n```",
        "layout": "src/minihttp/client.py\ntests/test_client.py",
        "rubric": ["pyright clean", "a test that fails closed on timeout", "no sleeps > 50ms in tests (mock time)"],
        "stretch": "OpenTelemetry span around each request (preview of Phase 12).",
    },
    "resources": {
        "official": ["[asyncio docs](https://docs.python.org/3/library/asyncio.html)", "[pydantic](https://docs.pydantic.dev/)", "[httpx](https://www.python-httpx.org/)"],
        "extra": ["[Real Python async primer](https://realpython.com/async-io-python/)", "Tenacity docs"],
        "papers": ["Not applicable — read PEP 654 (Exception Groups) if curious."],
    },
    "faq": [
        {"q": "Do I need to rewrite Pandas async?", "a": "No. Pandas is CPU/RAM. Keep it sync; run in a thread if you must, or don't put it on the hot request path."},
        {"q": "mypy or pyright?", "a": "Either. pyright is fast and what VS Code uses. Pick one in CI."},
        {"q": "Is FastAPI required for async?", "a": "No. asyncio works alone. FastAPI is Phase 3."},
    ],
    "debugging": [
        {
            "title": "coroutine was never awaited",
            "symptom": "RuntimeWarning and nothing happens.",
            "wrong": "Calling async def like a normal function runs it.",
            "see": "You forgot await or asyncio.run.",
            "fix": "await foo() inside async; asyncio.run(foo()) at the edge.",
            "prevent": "Type checkers warn if you configure them.",
        },
        {
            "title": "Tests hang",
            "symptom": "pytest never ends.",
            "wrong": "Forgot timeout; waited on a real network.",
            "see": "Which await never returns. Add timeout= to httpx.",
            "fix": "Mock network. Always set timeout.",
            "prevent": "pytest-timeout plugin.",
        },
    ],
    "mistakes": [
        {"title": "async def with time.sleep", "body": "You blocked the loop. All chats freeze.", "instead": "asyncio.sleep or to_thread."},
        {"title": "except Exception: pass around await", "body": "You swallowed CancelledError and KeyboardInterrupt cousins.", "instead": "Catch specific errors. Let CancelledError out."},
        {"title": "Building a list of all tokens then joining", "body": "You used extra RAM and delayed first byte.", "instead": "Yield chunks."},
    ],
    "prod_tips": {
        "cost": "Retries multiply cost. Cap them. Do not retry 400s from a bad prompt.",
        "latency": "First-byte latency matters more than total time for chat UX. Stream.",
        "reliability": "Timeouts + bounded retries + jitter. Measure retry rate.",
        "observability": "Log attempt number and latency. Later: traces.",
        "scaling": "One AsyncClient (connection pool) per process, not per request.",
        "checklist": ["timeouts", "retries capped", "pydantic on inputs and LLM outputs", "no time.sleep in async"],
    },
    "challenge": {
        "title": "100 concurrent fake streams",
        "body": "Simulate 100 clients consuming an async token generator. Prove memory stays flat vs the list-building version.",
        "constraints": ["Measure RSS", "No external model"],
        "success": "A table: N clients × pattern × peak RAM.",
    },
    "solutions": [
        {"id": "B1 windows", "hint": "for i in range(0, n-size+1, size-overlap): yield xs[i:i+size]", "approach": "Careful with overlap >= size (illegal). Validate."},
        {"id": "H1 cancel", "hint": "asyncio.timeout or task.cancel(); yield inside try; finally set flag.", "approach": "Don't catch BaseException unless you re-raise."},
    ],
    "code_files": {
        "ticket.py": '''"""Validate structured LLM-like JSON with Pydantic v2."""
from pydantic import BaseModel, Field, ValidationError


class Ticket(BaseModel):
    category: str = Field(pattern=r"^(billing|tech|other)$")
    priority: int = Field(ge=1, le=3)
    summary: str = Field(min_length=5, max_length=200)


def main() -> None:
    raw = '{"category":"billing","priority":1,"summary":"Invoice double charge"}'
    ticket = Ticket.model_validate_json(raw)
    print(ticket.category, ticket.priority)
    try:
        Ticket.model_validate_json('{"category":"banana","priority":9,"summary":"x"}')
    except ValidationError as exc:
        print("rejected", exc.error_count())


if __name__ == "__main__":
    main()
''',
        "retry.py": '''"""Exponential backoff with jitter. Production primitive."""
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
                except Exception as exc:
                    last = exc
                    time.sleep(base * (2**attempt) + random.random() * 0.05)
            assert last is not None
            raise last

        return wrapped

    return deco
''',
    },
}
