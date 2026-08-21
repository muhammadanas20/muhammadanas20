"""Framework-free agent loop."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Literal

ToolFn = Callable[..., str]


@dataclass
class Step:
    kind: Literal["tool", "text"]
    name: str | None = None
    args: dict[str, Any] | None = None
    text: str | None = None


TOOLS: dict[str, ToolFn] = {
    "add": lambda a, b: str(float(a) + float(b)),
}


def fake_model(n: int) -> Step:
    if n == 0:
        return Step("tool", name="add", args={"a": 2, "b": 3})
    return Step("text", text="2+3=5")


def run(max_steps: int = 4) -> str:
    for i in range(max_steps):
        step = fake_model(i)
        if step.kind == "tool":
            if step.name not in TOOLS:
                raise RuntimeError("unknown tool")
            print("tool", step.name, TOOLS[step.name](**(step.args or {})))
            continue
        return step.text or ""
    raise RuntimeError("max steps")


if __name__ == "__main__":
    print(run())
