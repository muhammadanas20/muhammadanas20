# Interview — Phase 9: Agents

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. What is an agent vs a chain?

**Expected answer (junior)**

A chain is a fixed sequence. An agent chooses tools at runtime. Chains are easier to test.

**Common mistakes**

Agent = chatbot.

**Senior-level discussion**

Graphs as the middle ground: bounded choices.
### Q2. How do you stop infinite tool use?

**Expected answer (junior)**

max_steps, timeouts, budgets, circuit breakers, no recursive 'search again' without a counter.

**Common mistakes**

Ask the model nicely.

**Senior-level discussion**

Hard termination in the runtime, not the prompt.
### Q3. Design a SQL agent.

**Expected answer (junior)**

Read-only role, SQL parser, LIMIT, allow-listed tables, traces, eval adversarial prompts, maybe only query builder not free SQL.

**Common mistakes**

Give it psql as root.

**Senior-level discussion**

Semantic layer, warehouse governance.
### Q4. LangGraph vs a for-loop?

**Expected answer (junior)**

Loop for simple. Graph when branches, retries, humans, multiple nodes need shared state.

**Common mistakes**

Always LangGraph to look senior.

**Senior-level discussion**

Operational complexity, versioning graphs.
### Q5. Multi-agent worth it?

**Expected answer (junior)**

When roles have different tools/prompts and a supervisor. Not for a single FAQ. Measure.

**Common mistakes**

Crew of 8 for everything.

**Senior-level discussion**

Debate vs handoff, cost, deadlock.


---

## Whiteboard prompts

- Draw a refund agent with HITL.
- SQL agent threat model.
- Convert a messy crew into one graph with 3 nodes.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for bounds, least privilege, and when they refuse to use an agent.
