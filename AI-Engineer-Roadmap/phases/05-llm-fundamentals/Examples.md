# Examples — Phase 5: LLM fundamentals

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. Structured output with a local-shaped client

Provider SDKs change. The pattern does not: schema in, validate out.

```python
"""code/structured.py"""
from __future__ import annotations

import json
from pydantic import BaseModel, Field, ValidationError

class Ticket(BaseModel):
    category: str = Field(pattern=r"^(billing|tech|other)$")
    priority: int = Field(ge=1, le=3)
    summary: str

def fake_model(prompt: str) -> str:
    # Pretend this string came from an LLM JSON mode
    return json.dumps({"category": "tech", "priority": 2, "summary": prompt[:80]})

def classify(text: str) -> Ticket:
    raw = fake_model(text)
    try:
        return Ticket.model_validate_json(raw)
    except ValidationError as exc:
        raise RuntimeError(f"model broke contract: {exc}") from exc

if __name__ == "__main__":
    print(classify("My login button 500s since the deploy"))

```

**What every interesting line is doing**

Ticket is the contract. fake_model stands in for OpenAI/Ollama. ValidationError becomes a runtime error you can retry or route.

**Expected output**

```text
category='tech' priority=2 summary='My login button 500s since the deploy'
```

**Dry run**

text → fake JSON → pydantic → Ticket. If category were 'banana', RuntimeError.

**Memory**

O(n) in the JSON string.

**Time complexity:** O(n) parse  
**Space complexity:** O(n)

**Alternatives**

Instructor library; OpenAI parse=; Anthropic structured; outlines/jsonformer for local models.

**Optimization**

Constrained decoding on local models to reduce retries.

---

### Example 2. A tiny tool loop

Agents (Phase 9) are this loop with extra state.

```python
"""code/tools.py"""
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

# A fake model turn: it 'decides' to call a tool then answer.
turns = [
    {"type": "tool", "name": "get_order", "args": {"order_id": "A1"}},
    {"type": "text", "content": "Order A1 is shipped."},
]
for turn in turns:
    if turn["type"] == "tool":
        print("tool", turn["name"], run_tool(turn["name"], turn["args"]))
    else:
        print("final", turn["content"])

```

**What every interesting line is doing**

Allow-list TOOLS. Never eval arbitrary names. The model proposes; your code dispatches.

**Expected output**

```text
tool get_order {"id": "A1", "status": "shipped"}\nfinal Order A1 is shipped.
```

**Dry run**

Loop turns. First dispatches get_order. Second prints. No infinite loop because we used a list, not while True — production needs a max_steps.

**Memory**

O(tools + conversation)

**Time complexity:** O(steps)  
**Space complexity:** O(steps)

**Alternatives**

OpenAI tool_calls array; LangGraph later; MCP later.

**Optimization**

Parallel tool calls when independent. Timeouts per tool.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
