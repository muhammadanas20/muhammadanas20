# Interview — Phase 13: Security

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. Explain prompt injection to a PM and to an engineer.

**Expected answer (junior)**

PM: social engineering of the bot. Engineer: untrusted tokens in the same context as instructions; models can't reliably separate them; so constrain tools and data.

**Common mistakes**

It's SQL injection with extra steps only.

**Senior-level discussion**

Indirect, exfil channels, multimodal.
### Q2. How do you secure a SQL tool?

**Expected answer (junior)**

Read-only role, parser, allow-listed tables, LIMIT, no stacked queries, RBAC, audit, tests.

**Common mistakes**

Ask the model to be careful.

**Senior-level discussion**

Semantic layer, warehouse policies.
### Q3. Retrieved wiki tells the model to ignore rules. Now what?

**Expected answer (junior)**

Untrusted wrapping, don't give write tools, maybe strip instruction-like lines, eval, maybe dual-LLM. Privilege stays in code.

**Common mistakes**

Ban wikis.

**Senior-level discussion**

Content security for corpora.
### Q4. What's in your threat model?

**Expected answer (junior)**

Assets, actors, injection, tenancy, secrets, logs, vendors, residual risk.

**Common mistakes**

We use HTTPS.

**Senior-level discussion**

Concrete.
### Q5. Guardrail model failed. Then?

**Expected answer (junior)**

It will. Design so failure isn't catastrophic: no high-priv tools, budgets, monitoring.

**Common mistakes**

Stack three more guardrails and relax.

**Senior-level discussion**

Blast radius.


---

## Whiteboard prompts

- Data flow of an indirect injection.
- RBAC matrix for support agent tools.
- What goes in traces vs what is redacted.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for least privilege and tests, not 'we prompt it to be safe'.
