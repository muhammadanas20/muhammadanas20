"""Naive RAG skeleton — retrieve, prompt, generate."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Hit:
    id: str
    text: str
    score: float


CORPUS = [
    Hit("h1", "A token is a piece of text the model bills and counts.", 0),
    Hit("h2", "Docker images are immutable snapshots.", 0),
    Hit("h3", "Redis is great for rate limits, not chat history.", 0),
]


def retrieve(q: str, k: int = 2) -> list[Hit]:
    words = q.lower().split()
    scored = [
        Hit(h.id, h.text, float(sum(w in h.text.lower() for w in words))) for h in CORPUS
    ]
    scored.sort(key=lambda x: -x.score)
    return scored[:k]


def prompt(q: str, hits: list[Hit]) -> str:
    src = "\n".join(f"[{h.id}] {h.text}" for h in hits)
    return (
        "Use ONLY the sources. If missing, say you don't know.\n"
        f"Sources:\n{src}\n\nQuestion: {q}\nAnswer:"
    )


def generate_fake(p: str) -> str:
    if "h1" in p and "token" in p.lower():
        return "A token is a billed text piece [h1]."
    return "I don't know."


if __name__ == "__main__":
    question = "What is a token?"
    hits = retrieve(question)
    print(generate_fake(prompt(question, hits)))
