"""Server-sent events stream of fake tokens."""
from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()


async def fake_tokens(prompt: str) -> AsyncIterator[bytes]:
    for word in f"You said: {prompt}".split():
        yield f"data: {word}\n\n".encode()
        await asyncio.sleep(0.05)
    yield b"data: [DONE]\n\n"


@app.post("/v1/chat/stream")
async def stream(payload: dict[str, str]) -> StreamingResponse:
    return StreamingResponse(
        fake_tokens(payload.get("prompt", "")),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
