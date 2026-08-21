"""Validate structured LLM-like JSON with Pydantic v2."""
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
