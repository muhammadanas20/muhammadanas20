"""Schema-validate a fake LLM JSON response."""
from __future__ import annotations

import json

from pydantic import BaseModel, Field, ValidationError


class Ticket(BaseModel):
    category: str = Field(pattern=r"^(billing|tech|other)$")
    priority: int = Field(ge=1, le=3)
    summary: str


def fake_model(prompt: str) -> str:
    return json.dumps({"category": "tech", "priority": 2, "summary": prompt[:80]})


def classify(text: str) -> Ticket:
    raw = fake_model(text)
    try:
        return Ticket.model_validate_json(raw)
    except ValidationError as exc:
        raise RuntimeError(f"model broke contract: {exc}") from exc


if __name__ == "__main__":
    print(classify("My login button 500s since the deploy"))
