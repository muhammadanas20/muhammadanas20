# Examples — Phase 9: Agents

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. Framework-free loop

If this is mysterious, LangGraph will be a religion.

```python
"""code/loop.py"""
from __future__ import annotations

import json
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
            assert step.name in TOOLS
            result = TOOLS[step.name](**(step.args or {}))
            print("tool", step.name, result)
            continue
        return step.text or ""
    raise RuntimeError("max steps")

if __name__ == "__main__":
    print(run())

```

**What every interesting line is doing**

Allow-list TOOLS. max_steps. fake_model stands in for the provider. Unknown tools would assert/fail closed.

**Expected output**

```text
tool add 5.0\n2+3=5
```

**Dry run**

i=0 tool add → i=1 text return.

**Memory**

O(steps)

**Time complexity:** O(max_steps)  
**Space complexity:** O(steps) if you stored history

**Alternatives**

LangGraph StateGraph with a tools node.

**Optimization**

Stop early. Parallel tools when independent.

---

### Example 2. Safe SQL wrapper

The SQL agent project in one function.

```python
"""code/safe_sql.py"""
from __future__ import annotations

FORBIDDEN = ("drop", "delete", "update", "insert", "alter", "truncate", "grant")

def guard_sql(sql: str, limit: int = 50) -> str:
    s = sql.strip().rstrip(";")
    low = s.lower()
    if not low.startswith("select"):
        raise ValueError("only SELECT")
    if any(w in low.split() for w in FORBIDDEN):
        raise ValueError("forbidden keyword")
    if " limit " not in low:
        s = f"{s} LIMIT {limit}"
    return s

```

**What every interesting line is doing**

Fail closed. Force LIMIT. Keyword block is not a full parser — production uses a real SQL parser and a read-only role. Defense in depth.

**Expected output**

```text
guard_sql('SELECT * FROM orders') → SELECT * FROM orders LIMIT 50
```

**Dry run**

DROP → error. SELECT without limit → append.

**Memory**

O(len(sql))

**Time complexity:** O(n)  
**Space complexity:** O(n)

**Alternatives**

sqlglot parse; Postgres role with SELECT only; query builder instead of free SQL.

**Optimization**

Prepared statements. Column allow-lists per tenant.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
