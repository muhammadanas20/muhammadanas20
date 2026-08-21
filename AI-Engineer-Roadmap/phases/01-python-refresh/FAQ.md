# FAQ — Phase 1: Python refresh

### Do I need to rewrite Pandas async?

No. Pandas is CPU/RAM. Keep it sync; run in a thread if you must, or don't put it on the hot request path.

### mypy or pyright?

Either. pyright is fast and what VS Code uses. Pick one in CI.

### Is FastAPI required for async?

No. asyncio works alone. FastAPI is Phase 3.

Didn't see your question? Open an issue. Beginner questions are first-class.
