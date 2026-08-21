# Interview — Phase 12: Production AI / LLMOps

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. What do you monitor for an LLM app?

**Expected answer (junior)**

Latency, errors, tokens, cost, cache, fallback, eval scores, retrieval empty rate — not only 500s.

**Common mistakes**

CPU only.

**Senior-level discussion**

SLOs and quality error budgets.
### Q2. How do you eval in CI?

**Expected answer (junior)**

Frozen JSONL, pinned model, threshold, fail build. Separate holdout.

**Common mistakes**

We eyeball on Friday.

**Senior-level discussion**

Flakes, cost of CI, sampling.
### Q3. Design caching.

**Expected answer (junior)**

Embedding cache always. Exact answer cache with TTL + versions + tenant. Semantic cache only if safe.

**Common mistakes**

Cache everything globally forever.

**Senior-level discussion**

Invalidation on ingest.
### Q4. Provider is down.

**Expected answer (junior)**

Timeouts, retries with jitter, fallback model, degrade to retrieval-only snippets, status page.

**Common mistakes**

Wait.

**Senior-level discussion**

Multi-vendor, queues.
### Q5. Cost exploded.

**Expected answer (junior)**

Traces: loops, k too big, no cache, retries on 400s, agent hops. Add budgets.

**Common mistakes**

Buy more credits first.

**Senior-level discussion**

Unit economics per feature.


---

## Whiteboard prompts

- SLO dashboard boxes for a RAG API.
- Cache key design for multi-tenant docs.
- CI eval pipeline.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for quality+cost+latency as first-class, traces, pinned evals.
