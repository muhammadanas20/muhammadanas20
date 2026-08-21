"""Bounded allow-listed tool loop."""
from __future__ import annotations

from collections.abc import Callable
from typing import Any

Tool = Callable[..., str]
TOOLS: dict[str, Tool] = {}


def register(name: str, fn: Tool) -> None:
    TOOLS[name] = fn


def run_tool(name: str, args: dict[str, Any]) -> str:
    if name not in TOOLS:
        return f'{{"error":"unknown tool {name}"}}'
    return TOOLS[name](**args)


def run_agent(model_turn, max_steps: int = 6) -> str:
    history: list[dict[str, Any]] = []
    for _ in range(max_steps):
        step = model_turn(history)
        if step.get("type") == "tool":
            result = run_tool(step["name"], step.get("args") or {})
            history.append({"tool": step["name"], "result": result})
            continue
        return str(step.get("text", ""))
    raise RuntimeError("max steps exceeded")
