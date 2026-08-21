"""Heading-aware Markdown chunker."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Chunk:
    heading: str
    text: str


def chunk_markdown(md: str, max_chars: int = 800) -> list[Chunk]:
    chunks: list[Chunk] = []
    heading = "root"
    buf: list[str] = []

    def flush() -> None:
        text = "\n".join(buf).strip()
        if text:
            chunks.append(Chunk(heading=heading, text=text))
        buf.clear()

    for line in md.splitlines():
        if line.startswith("#"):
            flush()
            heading = line.lstrip("#").strip() or heading
            continue
        buf.append(line)
        if sum(len(x) for x in buf) >= max_chars:
            flush()
    flush()
    return chunks
