# Interview — Phase 10: Model Context Protocol (MCP)

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. Why MCP?

**Expected answer (junior)**

Standardize tool/resource plugs so N clients and M servers do not need N×M adapters.

**Common mistakes**

It's just another agent framework.

**Senior-level discussion**

Compare to OpenAPI for HTTP, LSP for language servers.
### Q2. Tool vs resource vs prompt?

**Expected answer (junior)**

Tool=action, resource=readable context, prompt=server-provided template.

**Common mistakes**

All the same.

**Senior-level discussion**

When to fetch a resource vs stuffing it always.
### Q3. Security issues?

**Expected answer (junior)**

Local servers inherit user perms; remote needs auth; prompt injection via resources; secret files; destructive tools without approval.

**Common mistakes**

MCP is safe because it's a spec.

**Senior-level discussion**

Sandbox, approval UX, audit.
### Q4. When would you not use it?

**Expected answer (junior)**

One function, one service. Or ultra-low latency inner loop where RPC is overhead.

**Common mistakes**

Always MCP everything.

**Senior-level discussion**

Internal library vs protocol boundary.
### Q5. How does it relate to agents?

**Expected answer (junior)**

Agents consume tools. MCP is how tools are discovered and called across hosts.

**Common mistakes**

MCP replaces LangGraph.

**Senior-level discussion**

Agent runtime + MCP servers as the tool layer.


---

## Whiteboard prompts

- Sequence of initialize → list_tools → call_tool.
- Threat model of an MCP server over prod Postgres.
- Where MCP sits vs FastAPI vs LangGraph.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for protocol vs model vs framework, and security of the plug.
