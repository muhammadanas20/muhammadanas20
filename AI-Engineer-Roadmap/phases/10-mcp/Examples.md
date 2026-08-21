# Examples — Phase 10: Model Context Protocol (MCP)

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. A tiny in-process MCP-shaped registry

The protocol is JSON-RPC; the idea is a catalog of tools.

```python
"""code/catalog.py"""
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

cat = Catalog()
cat.add(Tool("ping", "Health", lambda: "pong"))
print(cat.list_tools())
print(cat.call("ping"))

```

**What every interesting line is doing**

Discovery (list) + dispatch (call) is what a client needs. Real MCP wraps this in JSON-RPC + schema.

**Expected output**

```text
[{'name': 'ping', ...}]\npong
```

**Dry run**

Register ping. List. Call.

**Memory**

O(tools)

**Time complexity:** O(1) dispatch  
**Space complexity:** O(tools)

**Alternatives**

Official SDK.

**Optimization**

This is a teaching model, not a replacement for the SDK.

---

### Example 2. stdio hygiene

The #1 MCP server bug.

```python
"""code/stdio_hygiene.py"""
import sys

def log(msg: str) -> None:
    # stdout is the protocol. Logs MUST go to stderr.
    print(msg, file=sys.stderr)

log("server starting")
# print("hello")  # would break JSON-RPC on stdio

```

**What every interesting line is doing**

Clients parse stdout as messages. A stray print corrupts the stream.

**Expected output**

```text
server starting  (on stderr)
```

**Dry run**

log writes to stderr. stdout remains clean.

**Memory**

O(1)

**Time complexity:** O(1)  
**Space complexity:** O(1)

**Alternatives**

Structured logging library with stream=stderr.

**Optimization**

Don't debug-print in tool handlers to stdout either.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
