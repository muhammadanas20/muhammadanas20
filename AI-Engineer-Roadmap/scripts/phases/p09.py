from make_phase import C, E, EX, I, Q, asg, drill, mp, phase, th

PHASE = phase(
    num="9",
    title="Agents",
    tagline="Multi-step work with tools. Also: when an agent is the wrong idea.",
    hours="14-21 days",
    difficulty="Hard",
    exit_ticket="An agent that queries SQL safely, logs every tool call, and cannot DROP TABLE.",
    objectives=[
        "Write a tool loop with no framework.",
        "Add max steps, timeouts, and allow-listed tools.",
        "Compare LangGraph, PydanticAI, CrewAI, OpenAI Agents SDK honestly.",
        "Implement memory that is not 'stuff the whole chat into the prompt'.",
        "Know planning vs reacting vs graph state machines.",
    ],
    prerequisites=["Phases 5 and 8. FastAPI + SQL strongly recommended."],
    topics=["Tool calling", "LangGraph", "PydanticAI", "CrewAI", "OpenAI Agents SDK", "Memory", "Planning", "Reflection"],
    nav="[Home](../../README.md) · Prev: [Phase 8](../08-rag/) · Next: [Phase 10 · MCP](../10-mcp/)",
    theory=th(
        intro="""An **agent** is a loop:

```
while not done and steps < max:
    model decides: answer or call tool
    if tool: run it, append result
    if answer: return
```

That is the whole trick.

Frameworks add graphs, memory, multi-agent handoffs, and a lot of magic. You must be able to draw the loop without them.

Most 'agent' demos should have been a RAG chain or a cron job.""",
        one_liner="An agent is a bounded tool loop, not a personality.",
        why="""Users want: 'refund order 123 if it is eligible, else explain policy.'

That needs **tools** (get_order, get_policy, create_refund) and **rules** (no refunds after 30 days), not a bigger prompt.

If you cannot bound the loop, you will pay for infinite tool calls. If you cannot restrict tools, the model will try `rm -rf`.""",
        if_missing="you would wrap ChatGPT around your database and hope.",
        analogy="""A junior employee with a phone and a badge.

- **Tools** = apps on the phone (CRM, calendar). The badge says which apps exist.
- **Loop** = they may call two apps then reply.
- **Max steps** = they cannot sit on hold forever on your dime.
- **Allow-list** = the badge does not include 'wire transfer'.
- **Memory** = a notebook (DB), not trying to remember every customer in RAM.
- **Graph (LangGraph)** = a flowchart on the wall: intake → verify → act → done.
- **Multi-agent** = specialists (researcher, writer) passing a folder. Overhead. Sometimes worth it.
- **Reflection** = a second pass: 'did I actually verify eligibility?'""",
        visual="""```mermaid
flowchart TD
  S[Start] --> M[Model]
  M -->|tool_call| T[Run tool]
  T --> M
  M -->|final| E[End]
  M -->|steps>max| X[Stop / escalate]
```""",
        architecture="""```mermaid
flowchart LR
  User --> API
  API --> Graph[LangGraph or loop]
  Graph --> Tools
  Tools --> SQL[(read-only DB)]
  Tools --> RAG
  Tools --> HTTP
  Graph --> Mem[(Postgres memory)]
  Graph --> Trace
```""",
        beginner="""**Tool:** a Python function with a JSON schema (name, description, parameters).

**Tool loop:** see intro. You implement `max_steps` (3–8 typical).

**ReAct:** Reason + Act — the model writes a thought then an action. The paper is Yao et al. 2022. Modern tool APIs often skip explicit 'thought' tokens but the idea remains.

**When not to use an agent:**
- One retrieve-then-answer (RAG)
- A deterministic workflow you can code
- You cannot define tools clearly

**Memory types:**
- Short-term: the current transcript (context window)
- Long-term: retrieved notes / user profile in a DB
- Episodic: 'last time this user tried X'""",
        intermediate="""**LangGraph:** you define a state dict and nodes and edges (including cycles). Best when the flow is a state machine: retry, human approval, branches.

**PydanticAI:** pythonic, type-heavy agents. Pleasant if you already love pydantic.

**CrewAI:** role-playing multi-agent. Great demos. Easy to over-engineer.

**OpenAI Agents SDK:** vendor-shaped. Fine inside their ecosystem. Keep a thin interface.

**Planning:** outline steps first (plan-and-execute). Helps long tasks; can be brittle if the plan is wrong.

**Reflection:** a second model call critiques the first. Cost ×2. Use on high-stakes steps only.

**Human-in-the-loop:** graph interrupts before `create_refund`.""",
        advanced="""**State reducers** in graphs (how messages append).

**Parallel tool calls.**

**Computer-use / browser agents:** high blast radius. Sandbox.

**Multi-agent protocols:** handoff vs debate vs supervisor. Supervisor is the usual production shape.

**Eval of agents:** trajectory eval (did it call the right tools in order), not just final BLEU. Golden paths + adversarial paths.

**Deterministic cores:** encode refund eligibility in Python; let the model fill slots, not invent policy.""",
        production="""Allow-list tools. Read-only DB roles. Row limits. Timeouts per tool. Idempotency. Trace every call. Budget per request. Circuit breaker if a tool is down. Never give `shell` in prod.

A SQL agent that runs `EXPLAIN` or a dry-run first is senior. A SQL agent that concatenates user text into SQL is a CVE.""",
        when="Multi-step, tool-using tasks with unclear path but clear tools and stop conditions.",
        when_not="Single-hop RAG. ETL. Anything you can write as a 40-line function. Unbounded 'research the internet forever'.",
        code_preview='''for _ in range(MAX):
    msg = model(history, tools)
    if msg.tool:
        history.append(run(msg.tool))
    else:
        return msg.text
raise Timeout
''',
        code_notes="This loop is the curriculum. Frameworks decorate it.",
        ex_b="Two tools: add(a,b) and now(). Loop with max 4.",
        ex_m="LangGraph: node retrieve → node generate, with a retry edge.",
        ex_h="SQL agent on a toy DB with SELECT-only, LIMIT injected, blocklist DDL.",
        project="SQL Agent — PROJECTS/04-sql-agent.",
        interview_preview="What is an agent? When not to use one? How to stop loops? How to safe SQL?",
        flash_sample="**Q:** Does the model execute tools?\n**A:** No. Your code does.",
        mistakes_preview="Uncapped loops. Shell tool. Multi-agent for a FAQ. Memory = whole history forever.",
        debug_preview="Tool args JSON invalid. Infinite search-search-search. Agent ignores tool error and invents.",
        best="Loop first, graph if state is real, allow-list, max steps, traces, deterministic policy in code.",
        industry="LangGraph is the most common production graph in Python circa 2025–2026. Many teams still use a 40-line loop. Both are valid.",
        perf="Parallel tools. Smaller models for routing. Don't reflect every turn.",
        security="Least privilege tools. No secret values in tool results if avoidable. Injection via tool output (Phase 13).",
        refs="- ReAct 2022\n- Anthropic: Building effective agents\n- LangGraph docs\n- OpenAI agents guide",
        further="CrewAI docs (comparison). PydanticAI docs. MCP next phase.",
    ),
    examples=[
        EX(
            title="Framework-free loop",
            why="If this is mysterious, LangGraph will be a religion.",
            code='''"""code/loop.py"""
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
''',
            line_by_line="Allow-list TOOLS. max_steps. fake_model stands in for the provider. Unknown tools would assert/fail closed.",
            output="tool add 5.0\\n2+3=5",
            dry_run="i=0 tool add → i=1 text return.",
            memory="O(steps)",
            time="O(max_steps)",
            space="O(steps) if you stored history",
            alternatives="LangGraph StateGraph with a tools node.",
            optimization="Stop early. Parallel tools when independent.",
        ),
        EX(
            title="Safe SQL wrapper",
            why="The SQL agent project in one function.",
            code='''"""code/safe_sql.py"""
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
''',
            line_by_line="Fail closed. Force LIMIT. Keyword block is not a full parser — production uses a real SQL parser and a read-only role. Defense in depth.",
            output="guard_sql('SELECT * FROM orders') → SELECT * FROM orders LIMIT 50",
            dry_run="DROP → error. SELECT without limit → append.",
            memory="O(len(sql))",
            time="O(n)",
            space="O(n)",
            alternatives="sqlglot parse; Postgres role with SELECT only; query builder instead of free SQL.",
            optimization="Prepared statements. Column allow-lists per tenant.",
        ),
    ],
    practice=[
        drill("Loop on paper", "Write the while loop from memory. Include max steps.", "Matches Theory."),
        drill("Deny by default", "List 10 tools a support agent might want. Cross out 7.", "Least privilege."),
        drill("LangGraph tutorial", "Official shortest graph. Then rewrite it as a loop. Which is clearer?", "A paragraph."),
    ],
    exercises={
        "beginner": [
            E("Two-tool loop", "add and now, real or fake model.", "max_steps test."),
            E("Unknown tool", "Model asks for shell. You return error JSON, do not crash.", "Fail closed."),
        ],
        "medium": [
            E("LangGraph retry", "A node fails, edge retries once, then ends.", "State includes attempt count."),
            E("Memory", "Persist last 5 facts per user in Postgres, retrieve into system prompt.", "Not the whole history forever."),
        ],
        "hard": [
            E("SQL agent", "Read-only, LIMIT, traces, 10 adversarial prompts.", "Zero DDL success."),
            E("Supervisor two-agent", "Researcher + writer with a hard turn cap.", "Cost log."),
        ],
    },
    assignments=[
        asg(
            "sql-agent",
            "1 week",
            "PROJECTS/04-sql-agent: natural language to guarded SELECT, FastAPI, traces, adversarial test file.",
            ["app", "tests/adversarial.txt", "README threat model"],
            ["read-only role", "limit", "max steps", "no DROP"],
        )
    ],
    quiz=[
        Q("An agent is best described as", "A smarter LLM", "A bounded tool-using loop", "A vector DB", "Docker Compose", "B", "Loop."),
        Q("Who executes tools?", "The GPU", "Your application code", "The tokenizer", "Nginx", "B", "You do."),
        Q("Uncapped loops", "Are fine", "Can loop until money dies", "Improve safety", "Are required by ReAct", "B", "Cap them."),
        Q("SQL agent should", "Use admin role", "Use read-only + guards", "String-concat user SQL as root", "Drop indexes for speed", "B", "Least privilege."),
        Q("LangGraph is useful when", "You need a state machine with cycles", "You print hello", "You store vectors", "You write CSS", "A", "Graphs."),
        Q("Multi-agent systems", "Always beat one agent", "Add overhead; use with a reason", "Replace RAG", "Are illegal", "B", "Overhead."),
        Q("Reflection costs", "Nothing", "Extra model calls", "Only RAM", "A Docker layer", "B", "Tokens."),
        Q("Memory should be", "Infinite prompt", "Structured and retrieved", "In the Dockerfile", "Temperature", "B", "Retrieve."),
        Q("Human-in-the-loop is for", "Every token", "High-impact actions (refunds, emails)", "Cosine", "HNSW", "B", "Stakes."),
        Q("A FAQ bot should be", "A 12-agent crew", "Usually RAG, not an agent", "A SQL dropper", "Uncapped search", "B", "Don't agent-wash."),
    ],
    flashcards=[
        C("Define agent.", "Bounded loop of model + tools."),
        C("Max steps why?", "Cost, loops, runaway."),
        C("ReAct?", "Reason + Act pattern."),
        C("Allow-list?", "Only registered tools run."),
        C("LangGraph?", "State graph with nodes/edges, can cycle."),
        C("When not agent?", "Single hop, deterministic code, RAG FAQ."),
        C("Safe SQL?", "Read-only role, parse, LIMIT, no DDL."),
        C("HITL?", "Human approval before a tool."),
        C("Trajectory eval?", "Score the tool path, not just the final sentence."),
        C("Supervisor pattern?", "One agent routes to specialists."),
    ],
    interview=[
        I("What is an agent vs a chain?", "A chain is a fixed sequence. An agent chooses tools at runtime. Chains are easier to test.", "Agent = chatbot.", "Graphs as the middle ground: bounded choices."),
        I("How do you stop infinite tool use?", "max_steps, timeouts, budgets, circuit breakers, no recursive 'search again' without a counter.", "Ask the model nicely.", "Hard termination in the runtime, not the prompt."),
        I("Design a SQL agent.", "Read-only role, SQL parser, LIMIT, allow-listed tables, traces, eval adversarial prompts, maybe only query builder not free SQL.", "Give it psql as root.", "Semantic layer, warehouse governance."),
        I("LangGraph vs a for-loop?", "Loop for simple. Graph when branches, retries, humans, multiple nodes need shared state.", "Always LangGraph to look senior.", "Operational complexity, versioning graphs."),
        I("Multi-agent worth it?", "When roles have different tools/prompts and a supervisor. Not for a single FAQ. Measure.", "Crew of 8 for everything.", "Debate vs handoff, cost, deadlock."),
    ],
    whiteboard=[
        "Draw a refund agent with HITL.",
        "SQL agent threat model.",
        "Convert a messy crew into one graph with 3 nodes.",
    ],
    interview_listen="bounds, least privilege, and when they refuse to use an agent",
    cheatsheet={
        "remember": "Loop + allow-list + max steps. You run tools. SQL is read-only. Graphs when state is real.",
        "bash": "pytest tests/test_sql_guard.py",
        "python": "for i in range(MAX):\n    ...",
        "decisions": "FAQ → RAG. Multi-step tools → agent. Known flowchart → graph or even plain code.",
        "numbers": "max_steps 3–8. Tool timeout 5–30s. Reflection only on high stakes.",
        "do_not": "shell in prod. Uncapped. Admin DB. Multi-agent theater.",
    },
    miniproject=mp(
        name="sql-agent",
        time="3–5 days",
        difficulty="Hard",
        why="Interviewers love this because it is easy to do unsafely.",
        story="I ask 'top 5 customers by spend' and get a table, not a dropped database.",
        must=["guard_sql", "read-only", "max steps", "logs", "adversarial tests"],
        should=["FastAPI", "LangGraph version compared to loop"],
        wont=["write queries in prod"],
        architecture="```mermaid\nflowchart LR\nQ --> Agent --> Guard --> PG\n```",
        layout="../../PROJECTS/04-sql-agent/",
        rubric=["0 DDL", "LIMIT present", "README threat model"],
        stretch="EXPLAIN before execute.",
    ),
    resources={
        "official": ["LangGraph", "PydanticAI", "OpenAI Agents SDK", "Anthropic effective agents"],
        "extra": ["CrewAI docs for contrast", "ReAct paper"],
        "papers": ["ReAct 2022", "Toolformer 2023"],
    },
    faq=[
        {"q": "Must I learn all four frameworks?", "a": "Loop + one graph (LangGraph). Skim the others to speak the names honestly."},
        {"q": "Is AutoGPT back?", "a": "Unbounded agents keep failing in prod. Bounded graphs win."},
        {"q": "Memory library?", "a": "Start with Postgres. Vector memory is just RAG over notes."},
    ],
    debugging=[
        {
            "title": "Invalid tool JSON",
            "symptom": "Exception in dispatcher.",
            "wrong": "Trusting args.",
            "see": "Raw tool_call.",
            "fix": "json.loads in try; return error to model; pydantic schemas.",
            "prevent": "Structured tool APIs.",
        },
        {
            "title": "Loop of searches",
            "symptom": "Same query 8 times.",
            "wrong": "No step counter; model 'try again'.",
            "see": "Trace.",
            "fix": "max_steps, detect duplicate tool args, then stop.",
            "prevent": "Runtime guards > prompt guards.",
        },
    ],
    mistakes=[
        {"title": "Agent-washing a form", "body": "A form with 3 fields became a 6-agent crew.", "instead": "HTML form or a chain."},
        {"title": "Policy in the prompt only", "body": "Model refunds anyway.", "instead": "Eligibility in Python; model proposes."},
        {"title": "Swallowing tool errors", "body": "Model invents the order status.", "instead": "Pass the error back; maybe stop."},
    ],
    prod_tips={
        "cost": "Each hop is a full model fee. Budget hops. Smaller model for tool choice.",
        "latency": "Parallel tools. Stream the final answer only.",
        "reliability": "Timeouts, retries on tools not on non-idempotent POSTs, fallback to human.",
        "observability": "Trace tool name, args (redacted), duration, result size.",
        "scaling": "Agents are QPS-expensive. Queue. Don't hide a batch job in an agent.",
        "checklist": ["max_steps", "allow-list", "timeouts", "least privilege", "traces", "adversarial tests"],
    },
    challenge={
        "title": "Same task, three runtimes",
        "body": "Loop, LangGraph, PydanticAI. Same tools. Compare lines of code, latency, debuggability.",
        "constraints": ["Identical eval tasks", "Honest winner"],
        "success": "A memo you could send to a tech lead.",
    },
    solutions=[
        {"id": "H1 SQL", "hint": "DB role + guard_sql + parser.", "approach": "Tests: DROP, comments, stacked queries, UNION. All fail."},
        {"id": "M1 graph", "hint": "attempt in state, conditional edge.", "approach": "Keep state typed."},
    ],
    code_files={
        "loop.py": '''"""Framework-free agent loop."""
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
''',
        "safe_sql.py": '''"""Defense-in-depth SQL guard. Still use a read-only DB role."""
from __future__ import annotations

FORBIDDEN = ("drop", "delete", "update", "insert", "alter", "truncate", "grant")


def guard_sql(sql: str, limit: int = 50) -> str:
    s = sql.strip().rstrip(";")
    low = s.lower()
    if not low.startswith("select"):
        raise ValueError("only SELECT")
    if any(w in low.split() for w in FORBIDDEN):
        raise ValueError("forbidden keyword")
    if " limit " not in f" {low} ":
        s = f"{s} LIMIT {limit}"
    return s
''',
    },
)
