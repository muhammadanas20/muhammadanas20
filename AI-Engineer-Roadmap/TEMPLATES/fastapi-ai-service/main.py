"""Minimal AI-ready FastAPI shell."""
from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI(title="ai-service")


class ChatIn(BaseModel):
    prompt: str


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


async def tokens(prompt: str) -> AsyncIterator[bytes]:
    for word in f"echo: {prompt}".split():
        yield f"data: {word}\n\n".encode()
        await asyncio.sleep(0.03)
    yield b"data: [DONE]\n\n"


@app.post("/v1/chat/stream")
async def chat_stream(body: ChatIn) -> StreamingResponse:
    return StreamingResponse(
        tokens(body.prompt),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
