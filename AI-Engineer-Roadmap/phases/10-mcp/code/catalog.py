"""Discovery + dispatch — the MCP idea without the wire protocol."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class Tool:
    name: str
    description: str
    handler: Callable[..., str]


class Catalog:
    def __init__(self) -> None:
        self.tools: dict[str, Tool] = {}

    def add(self, tool: Tool) -> None:
        self.tools[tool.name] = tool

    def list_tools(self) -> list[dict[str, str]]:
        return [{"name": t.name, "description": t.description} for t in self.tools.values()]

    def call(self, name: str, **args: Any) -> str:
        if name not in self.tools:
            raise KeyError(name)
        return self.tools[name].handler(**args)


if __name__ == "__main__":
    cat = Catalog()
    cat.add(Tool("ping", "Health", lambda: "pong"))
    print(cat.list_tools())
    print(cat.call("ping"))
