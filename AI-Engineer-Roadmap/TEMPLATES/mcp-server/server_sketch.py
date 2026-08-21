"""MCP-shaped catalog. Swap in the official SDK when you implement Phase 10."""
from __future__ import annotations

import sys
from collections.abc import Callable
from typing import Any


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


class Server:
    def __init__(self) -> None:
        self.tools: dict[str, Callable[..., str]] = {}

    def tool(self, name: str, fn: Callable[..., str]) -> None:
        self.tools[name] = fn

    def call(self, name: str, **kwargs: Any) -> str:
        if name not in self.tools:
            raise KeyError(name)
        return self.tools[name](**kwargs)


if __name__ == "__main__":
    s = Server()
    s.tool("ping", lambda: "pong")
    log("tools: " + ",".join(s.tools))
    print(s.call("ping"))  # demo only; real stdio servers must not print non-protocol data
