# Quiz — Phase 13: Security

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

1. Direct injection is
    A) SQL only
    B) User text overriding instructions
    C) A Docker attack only
    D) HNSW
2. Indirect injection lives in
    A) Your Dockerfile always
    B) Retrieved docs / tool output / web pages
    C) TLS certs
    D) JWT alg none only
3. Best control for dangerous actions
    A) A longer system prompt
    B) Don't ship the tool / HITL / RBAC
    C) Higher temperature
    D) More chunks
4. API keys in system prompts
    A) Convenient
    B) A leak waiting to happen
    C) Encrypted by the model
    D) Required for tools
5. RBAC is
    A) Random bytes
    B) Role-based access control
    C) A reranker
    D) A PaaS
6. Guardrails are
    A) Perfect
    B) Helpful layers that can be bypassed
    C) Illegal
    D) Embeddings
7. PII in Langfuse
    A) Always fine
    B) Needs redaction and a contract
    C) Impossible
    D) A Docker flag
8. Tenant filter missing is
    A) A performance issue only
    B) A data breach class bug
    C) Fine in RAG
    D) A CSS bug
9. Shell tool in prod
    A) Senior
    B) Usually insane
    C) Required for MCP
    D) Faster RAG
10. System prompts should be assumed
    A) Secret forever
    B) Eventually public
    C) A substitute for auth
    D) Stored in Redis only

---

<details>
<summary>Answers (spoiler)</summary>

1. **B** — User box.
2. **B** — Data.
3. **B** — Blast radius.
4. **B** — Never.
5. **B** — Authz.
6. **B** — Depth.
7. **B** — Care.
8. **B** — Isolation.
9. **B** — No.
10. **B** — Don't put secrets there.

</details>
