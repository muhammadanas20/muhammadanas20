"""Toy model router."""


def route(question: str) -> str:
    q = question.lower()
    if len(q) < 40 or q.startswith(("hi", "hello", "thanks")):
        return "cheap"
    if any(w in q for w in ("legal", "medical", "refund policy")):
        return "strong"
    return "cheap"


if __name__ == "__main__":
    print(route("hi"), route("What is the refund policy for EU customers?"))
