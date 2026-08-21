from make_phase import C, E, EX, I, Q, asg, drill, mp, phase, th

PHASE = phase(
    num="10",
    title="Model Context Protocol (MCP)",
    tagline="A standard way to give models tools, resources, and prompts — with auth.",
    hours="7-10 days",
    difficulty="Hard",
    exit_ticket="A working MCP server consumed by a client (agent or IDE).",
    objectives=[
        "Explain why MCP exists (the N×M tools problem).",
        "Build a server that exposes tools and resources.",
        "Connect a client.",
        "Understand transports (stdio, HTTP/SSE).",
        "Think about authentication and least privilege.",
    ],
    prerequisites=["Phase 9 tool loops. You can write a Python package."],
    topics=["MCP protocol", "server", "client", "tools", "resources", "prompts", "auth"],
    nav="[Home](../../README.md) · Prev: [Phase 9](../09-agents/) · Next: [Phase 11 · Deployment](../11-deployment/)",
    theory=th(
        intro="""Every app reinvented 'how the model calls my functions.'

**Model Context Protocol (MCP)** is an open protocol (Anthropic-led, broadly adopted) so that:

- A **server** can expose tools, resources, and prompt templates
- Many **clients** (Claude Desktop, IDEs, your agent) can use them without custom glue each time

Think USB for model tools.

The spec will evolve. The idea — **standardize the plug** — will not.""",
        one_liner="MCP is a USB port for tools, files, and prompts that models can use.",
        why="""Without a protocol you write OpenAI tool schemas, then Anthropic tools, then LangChain tools, then a VS Code plugin. Four wrappers. One bug each.

With MCP, you write one server — e.g. 'query our read-only catalog' — and any MCP client can use it.

This is becoming a job-post keyword. You should have built one.""",
        if_missing="you would keep writing one-off tool wrappers per host.",
        analogy="""Power sockets.

- Before: every appliance ships its own generator (custom tool JSON per host).
- After: wall sockets (MCP) and adapters (clients).
- **Tools** = switches you can flip (functions).
- **Resources** = books on the shelf the model can read (files, tickets, schemas) without copying them into every prompt up front.
- **Prompts** = recipe cards the server offers ('explain this table').
- **Auth** = not every stranger can plug into the factory socket.""",
        visual="""```mermaid
flowchart LR
  C1[IDE client] --> S[MCP server]
  C2[Your FastAPI agent] --> S
  C3[Desktop app] --> S
  S --> DB[(Postgres)]
  S --> FS[Repo files]
  S --> API[Internal HTTP]
```""",
        architecture="""```mermaid
sequenceDiagram
  participant Client
  participant Server
  Client->>Server: initialize
  Client->>Server: list_tools
  Server-->>Client: tools[]
  Client->>Server: call_tool(name, args)
  Server-->>Client: result
  Client->>Server: read_resource(uri)
  Server-->>Client: contents
```""",
        beginner="""**Server:** a process that speaks MCP. In Python, official SDKs exist (`mcp` package). It declares tools (JSON schema), resources (URIs like `file://` or `postgres://`), and prompts.

**Client:** the host. It discovers tools and forwards model-requested calls to the server.

**Transport:**
- **stdio** — client spawns server as a subprocess, talks over stdin/stdout. Great for local IDE plugins.
- **HTTP / SSE / streamable HTTP** — remote servers.

**Tool vs resource:**
- Tool = verb (search, create_ticket)
- Resource = noun the model can read (schema.sql, ticket 55)

**You still write the Python that talks to Postgres.** MCP is the plug, not the database.""",
        intermediate="""**JSON-RPC** under the hood. Errors are structured.

**Sampling / roots / elicitation** — advanced parts of the spec; read when you need them.

**Prompts as products:** a server can expose `summarize_pr` with arguments.

**Composition:** an agent may attach many servers (filesystem, github, your company). Least privilege: don't attach filesystem+prod-db to a public agent.

**Versioning:** treat the server like an API. Breaking tool schemas break clients.""",
        advanced="""**Auth:** local stdio inherits your OS user (already scary — the server can do what you can do). Remote servers need OAuth / tokens / mTLS. Do not ship an unauthenticated HTTP MCP server on the public internet.

**Approval UX:** good clients ask before running a destructive tool.

**Sandboxing:** run servers as a less-privileged user. Containerize.

**The spec moves.** Read modelcontextprotocol.io on the week you implement. This course teaches the shape, not a frozen method list.""",
        production="""Company MCP servers:

- Live on private networks
- Authenticate
- Expose least tools
- Log every call
- Rate limit
- Have a human-readable catalog

IDE MCP is a productivity win and a data-leak risk (the model may see secrets in `.env` if you mount the whole repo). `.mcpignore` / careful roots.""",
        when="Reusable tools across hosts. IDE copilots over internal systems. Standardizing company tools.",
        when_not="A single internal function called from one FastAPI file — just a Python function. Don't MCP-wash it.",
        code_preview='''# Sketch — see current SDK for exact decorators
@server.tool()
def search_docs(query: str) -> str:
    """Search the internal wiki."""
    return retrieve(query)
''',
        code_notes="A tool is still an allow-listed function. MCP only standardizes discovery and calling.",
        ex_b="Filesystem MCP (official example) against this repo. List tools.",
        ex_m="Write a server with one tool `course_search` over Phase 6 index.",
        ex_h="Add a resource `schema://public` that returns SQL DDL. Auth token for HTTP transport.",
        project="Course MCP server — MiniProject.md.",
        interview_preview="What problem MCP solves. Tool vs resource. stdio vs HTTP. Auth concern.",
        flash_sample="**Q:** Is MCP a model?\n**A:** No. It is a protocol.",
        mistakes_preview="Exposing the whole filesystem. Unauthenticated HTTP. Duplicating 30 tools that should be one search. Ignoring spec updates.",
        debug_preview="Client doesn't see tools (initialize handshake). stdio logging broke JSON-RPC (never print to stdout).",
        best="Least privilege. Logs. Stdout is the protocol — logs go to stderr. Version schemas. Don't mount .env.",
        industry="Claude Desktop, various IDEs, OpenAI-adjacent hosts, internal agent platforms — all growing MCP support. Job posts in 2025–2026 mention it.",
        perf="Local stdio is cheap. Remote: same as any RPC. Don't stream 100MB resources into context.",
        security="Auth, sandbox, no secrets in resources, user approval for writes, audit log.",
        refs="- https://modelcontextprotocol.io\n- MCP GitHub org\n- Official Python SDK",
        further="Your IDE's MCP docs. Security write-ups on MCP prompt injection.",
    ),
    examples=[
        EX(
            title="A tiny in-process MCP-shaped registry",
            why="The protocol is JSON-RPC; the idea is a catalog of tools.",
            code='''"""code/catalog.py"""
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
''',
            line_by_line="Discovery (list) + dispatch (call) is what a client needs. Real MCP wraps this in JSON-RPC + schema.",
            output="[{'name': 'ping', ...}]\\npong",
            dry_run="Register ping. List. Call.",
            memory="O(tools)",
            time="O(1) dispatch",
            space="O(tools)",
            alternatives="Official SDK.",
            optimization="This is a teaching model, not a replacement for the SDK.",
        ),
        EX(
            title="stdio hygiene",
            why="The #1 MCP server bug.",
            code='''"""code/stdio_hygiene.py"""
import sys

def log(msg: str) -> None:
    # stdout is the protocol. Logs MUST go to stderr.
    print(msg, file=sys.stderr)

log("server starting")
# print("hello")  # would break JSON-RPC on stdio
''',
            line_by_line="Clients parse stdout as messages. A stray print corrupts the stream.",
            output="server starting  (on stderr)",
            dry_run="log writes to stderr. stdout remains clean.",
            memory="O(1)",
            time="O(1)",
            space="O(1)",
            alternatives="Structured logging library with stream=stderr.",
            optimization="Don't debug-print in tool handlers to stdout either.",
        ),
    ],
    practice=[
        drill("Read the spec intro", "modelcontextprotocol.io — tools, resources, prompts pages.", "You can sketch the handshake."),
        drill("Official quickstart", "Run a reference server. List tools from a client.", "Screenshot or log."),
        drill("stderr", "Add a print, watch the client break, then fix.", "Muscle memory."),
    ],
    exercises={
        "beginner": [
            E("Wrap ping", "MCP server with ping tool.", "A client can call it."),
            E("Resource", "Expose README.md as a resource URI.", "Client reads it."),
        ],
        "medium": [
            E("course_search tool", "Search this course Markdown.", "Returns top 3 snippets."),
            E("Prompt template", "Expose explain_phase(n).", "Client can get the prompt."),
        ],
        "hard": [
            E("HTTP + token", "Remote transport with Authorization header.", "Reject missing token."),
            E("Least privilege", "Two tools, only one enabled by config.", "Test both modes."),
        ],
    },
    assignments=[
        asg(
            "course-mcp",
            "1–2 days",
            "MCP server over this repo: search tool, resource per phase README, stderr logging, README with client config snippet.",
            ["server package", "example client config", "tests"],
            ["no stdout junk", "least privilege note", "works with one real client or a script client"],
        )
    ],
    quiz=[
        Q("MCP is", "A foundation model", "A protocol for tools/resources/prompts", "A vector DB", "A GPU driver", "B", "Protocol."),
        Q("stdio transport means", "HTTP", "Subprocess pipes", "SMTP", "Bluetooth", "B", "Local."),
        Q("Logs on stdio servers go to", "stdout", "stderr", "Redis", "S3", "B", "Keep stdout clean."),
        Q("A resource is", "A verb", "A readable noun/URI", "A Docker volume only", "A JWT always", "B", "Noun."),
        Q("A tool is", "A verb/function", "A PDF", "A CSS file", "HNSW", "A", "Verb."),
        Q("N×M problem", "GPUs vs RAM", "Many hosts × many tool integrations", "SQL joins", "RAG k", "B", "Why MCP exists."),
        Q("Unauthenticated public MCP HTTP", "Best practice", "Dangerous", "Required", "Faster", "B", "Don't."),
        Q("Mounting .env as a resource", "Helpful", "A secret leak", "Required by spec", "Encrypts automatically", "B", "Leak."),
        Q("Who runs the tool code?", "The LLM chip", "The MCP server process", "Nginx", "The embedder", "B", "Your server."),
        Q("MCP replaces RAG", "Yes", "No — it can expose retrieval as a tool", "Yes if k=50", "Only on Tuesdays", "B", "Complement."),
    ],
    flashcards=[
        C("MCP stands for?", "Model Context Protocol."),
        C("Three primitives?", "Tools, resources, prompts."),
        C("stdio vs HTTP?", "Local subprocess vs remote."),
        C("Why stderr?", "stdout is JSON-RPC."),
        C("USB analogy?", "Standard plug for model capabilities."),
        C("Auth on remote?", "Required. Tokens/OAuth/mTLS."),
        C("Least privilege?", "Fewest tools and narrowest filesystem roots."),
        C("Is MCP the model?", "No."),
        C("IDE risk?", "Model reads secrets in the repo."),
        C("When not MCP?", "Single internal function, one caller."),
    ],
    interview=[
        I("Why MCP?", "Standardize tool/resource plugs so N clients and M servers do not need N×M adapters.", "It's just another agent framework.", "Compare to OpenAPI for HTTP, LSP for language servers."),
        I("Tool vs resource vs prompt?", "Tool=action, resource=readable context, prompt=server-provided template.", "All the same.", "When to fetch a resource vs stuffing it always."),
        I("Security issues?", "Local servers inherit user perms; remote needs auth; prompt injection via resources; secret files; destructive tools without approval.", "MCP is safe because it's a spec.", "Sandbox, approval UX, audit."),
        I("When would you not use it?", "One function, one service. Or ultra-low latency inner loop where RPC is overhead.", "Always MCP everything.", "Internal library vs protocol boundary."),
        I("How does it relate to agents?", "Agents consume tools. MCP is how tools are discovered and called across hosts.", "MCP replaces LangGraph.", "Agent runtime + MCP servers as the tool layer."),
    ],
    whiteboard=[
        "Sequence of initialize → list_tools → call_tool.",
        "Threat model of an MCP server over prod Postgres.",
        "Where MCP sits vs FastAPI vs LangGraph.",
    ],
    interview_listen="protocol vs model vs framework, and security of the plug",
    cheatsheet={
        "remember": "USB for tools. stderr logs. Least privilege. Auth remote. Not a model.",
        "bash": "python -m my_mcp_server  # stdio\n# configure in client JSON",
        "python": "print(msg, file=sys.stderr)",
        "decisions": "Reusable across hosts → MCP. One caller → function.",
        "numbers": "Keep resource sizes prompt-small. Tool timeouts still apply.",
        "do_not": "stdout debug. Public unauth HTTP. Whole-home filesystem. .env resources.",
    },
    miniproject=mp(
        name="course-mcp",
        time="1–2 days",
        difficulty="Hard",
        why="Proof you can ship a protocol server, not only a notebook.",
        story="My IDE can search this course via MCP.",
        must=["search tool", "phase README resource", "stderr logging", "client config snippet"],
        should=["token auth if HTTP"],
        wont=["30 tools"],
        architecture="```mermaid\nflowchart LR\nIDE --> MCP --> Markdown\n```",
        layout="../../TEMPLATES/mcp-server/",
        rubric=["client can call", "README security section"],
        stretch="Resources for each phase Theory.md.",
    ),
    resources={
        "official": ["https://modelcontextprotocol.io", "Python SDK GitHub"],
        "extra": ["IDE MCP docs (Claude Desktop / Cursor / VS Code as of your date)"],
        "papers": ["n/a — read the spec"],
    },
    faq=[
        {"q": "MCP vs OpenAPI?", "a": "OpenAPI describes HTTP APIs for any client. MCP describes tools/resources for model hosts. You can wrap OpenAPI with MCP."},
        {"q": "MCP vs LangGraph tools?", "a": "LangGraph is a runtime. MCP is a distribution protocol. Use both: graph calls MCP tools."},
        {"q": "Do I need Anthropic?", "a": "No. MCP is open. Many hosts speak it."},
    ],
    debugging=[
        {
            "title": "Client shows zero tools",
            "symptom": "Server seems running.",
            "wrong": "Handshake failed; stdout polluted; wrong command path.",
            "see": "stderr logs; run server manually; validate JSON-RPC.",
            "fix": "Clean stdout, fix initialize, check config command/args.",
            "prevent": "A script client in tests.",
        },
        {
            "title": "Broken JSON",
            "symptom": "Parse errors in client.",
            "wrong": "print() in a tool.",
            "see": "Capture stdout.",
            "fix": "stderr only.",
            "prevent": "Lint for print.",
        },
    ],
    mistakes=[
        {"title": "MCP as a personality", "body": "It's plumbing.", "instead": "Talk about discovery and auth."},
        {"title": "One server with 80 tools", "body": "The model chooses poorly.", "instead": "Small servers per domain."},
        {"title": "No human approval for writes", "body": "IDE agent deletes files.", "instead": "Confirm UX + split read/write servers."},
    ],
    prod_tips={
        "cost": "Each tool result enters the prompt — keep results small.",
        "latency": "Local stdio is ms. Remote is network + tool time.",
        "reliability": "Version tools. Health tool. Timeouts.",
        "observability": "Log tool, args hash, duration, user.",
        "scaling": "Remote servers are just services. Same as FastAPI scale.",
        "checklist": ["stderr", "least privilege", "auth if remote", "no secrets", "tests with a fake client"],
    },
    challenge={
        "title": "Wrap your Phase 8 retriever as MCP",
        "body": "search + get_chunk(id) tools. Agent in Phase 9 uses them instead of in-process Python.",
        "constraints": ["Same eval questions still pass"],
        "success": "The protocol boundary didn't destroy quality.",
    },
    solutions=[
        {"id": "B1 ping", "hint": "Official SDK quickstart, change the function.", "approach": "Test with a 20-line JSON-RPC client if no UI."},
        {"id": "H1 auth", "hint": "Middleware on HTTP transport.", "approach": "401 without bearer."},
    ],
    code_files={
        "catalog.py": '''"""Discovery + dispatch — the MCP idea without the wire protocol."""
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
''',
        "stdio_hygiene.py": '''"""stdout is the protocol. Log to stderr."""
import sys


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


if __name__ == "__main__":
    log("server starting")
''',
    },
)
