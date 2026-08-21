"""Three functions you can test separately."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Hit:
    id: str
    text: str
    score: float


def retrieve(question: str, k: int = 5) -> list[Hit]:
    raise NotImplementedError("Phase 6–7")


def build_prompt(question: str, hits: list[Hit]) -> str:
    src = "\n".join(f"[{h.id}] {h.text}" for h in hits)
    return (
        "Use ONLY these sources. If missing, say you don't know.\n"
        f"{src}\n\nQuestion: {question}\nAnswer:"
    )


def generate(prompt: str) -> str:
    raise NotImplementedError("Phase 5")


def answer(question: str) -> tuple[str, list[str]]:
    hits = retrieve(question)
    text = generate(build_prompt(question, hits))
    return text, [h.id for h in hits]
