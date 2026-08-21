"""Allow-listed tool dispatch — the heart of agents."""
from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any

Tool = Callable[..., str]


def get_order(order_id: str) -> str:
    return json.dumps({"id": order_id, "status": "shipped"})


TOOLS: dict[str, Tool] = {"get_order": get_order}


def run_tool(name: str, args: dict[str, Any]) -> str:
    if name not in TOOLS:
        return json.dumps({"error": "unknown tool"})
    return TOOLS[name](**args)


def main() -> None:
    turns = [
        {"type": "tool", "name": "get_order", "args": {"order_id": "A1"}},
        {"type": "text", "content": "Order A1 is shipped."},
    ]
    for turn in turns:
        if turn["type"] == "tool":
            print("tool", turn["name"], run_tool(turn["name"], turn["args"]))
        else:
            print("final", turn["content"])


if __name__ == "__main__":
    main()
