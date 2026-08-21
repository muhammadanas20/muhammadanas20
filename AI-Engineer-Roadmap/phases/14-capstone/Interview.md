# Interview — Phase 14: Capstone

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. Tell me about your capstone.

**Expected answer (junior)**

Problem, user, architecture in 3 boxes, constraint, number, one failure, one next step. 90 seconds.

**Common mistakes**

I used LangChain and OpenAI and Docker and ...

**Senior-level discussion**

They will interrupt. Let them.
### Q2. What would you delete?

**Expected answer (junior)**

A component that didn't move the eval. Shows taste.

**Common mistakes**

Nothing it is perfect.

**Senior-level discussion**

Tradeoffs.
### Q3. A bug you hit?

**Expected answer (junior)**

A real one: SSE buffer, tenant leak test, chunking tables. How you saw it.

**Common mistakes**

It just worked.

**Senior-level discussion**

Debug story.
### Q4. How much does it cost?

**Expected answer (junior)**

Order-of-magnitude per 1k queries at chosen models. What you'd do if traffic ×10.

**Common mistakes**

I don't know I used free credits.

**Senior-level discussion**

Unit economics.
### Q5. Why not multi-agent?

**Expected answer (junior)**

If you chose RAG: because a chain met the eval. If you chose agent: because tools were real.

**Common mistakes**

Everyone uses agents.

**Senior-level discussion**

Taste.


---

## Whiteboard prompts

- Draw YOUR capstone in 8 boxes from SYSTEM_DESIGN_GUIDE.
- Show the eval loop.
- Show the threat model data flow.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for a finished story with a number and a limitation.
