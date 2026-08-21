"""PDF Chat skeleton — replace fakes with Phase 6–8 implementations."""
from __future__ import annotations

from dataclasses import dataclass

from fastapi import FastAPI, UploadFile
from pydantic import BaseModel

app = FastAPI(title="PDF Chat")


@dataclass
class Chunk:
    id: str
    page: int
    text: str


CHUNKS: list[Chunk] = []


class AskIn(BaseModel):
    question: str
    k: int = 4


class AskOut(BaseModel):
    answer: str
    citations: list[str]


@app.post("/ingest")
async def ingest(file: UploadFile) -> dict[str, int]:
    """Store extracted chunks in memory. Swap for a vector DB."""
    data = (await file.read()).decode("utf-8", errors="ignore")
    CHUNKS.clear()
    CHUNKS.append(Chunk(id="c1", page=1, text=data[:2000] or "empty"))
    return {"chunks": len(CHUNKS)}


def retrieve(question: str, k: int) -> list[Chunk]:
    # TODO: embeddings + vector search (Phase 6–7)
    return CHUNKS[:k]


def generate(question: str, hits: list[Chunk]) -> str:
    if not hits:
        return "I don't know."
    # TODO: real model call (Phase 5)
    return f"Based on {hits[0].id}: {hits[0].text[:180]}"


@app.post("/ask", response_model=AskOut)
def ask(body: AskIn) -> AskOut:
    hits = retrieve(body.question, body.k)
    answer = generate(body.question, hits)
    cites = [h.id for h in hits]
    return AskOut(answer=answer, citations=cites)


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}
