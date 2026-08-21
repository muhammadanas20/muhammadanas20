# Interview — Phase 7: Vector databases

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. pgvector vs dedicated vector DB?

**Expected answer (junior)**

pgvector: one system, transactions, smaller scale. Dedicated: heavier filters, scale, ANN knobs. Start with pgvector if already on PG.

**Common mistakes**

Always Pinecone. Never pgvector.

**Senior-level discussion**

Numbers: millions vs tens of millions, team ops skill, hybrid, cost.
### Q2. How do you isolate tenants?

**Expected answer (junior)**

Filter every query; tests that fail when filter omitted; maybe separate collections or RLS.

**Common mistakes**

We remember to filter.

**Senior-level discussion**

Crypto isolation, per-tenant encryption keys, query planner leaks.
### Q3. What is HNSW?

**Expected answer (junior)**

A graph ANN index. Faster than brute force, approximate. Parameters trade recall and memory.

**Common mistakes**

A neural net. A hash of the prompt.

**Senior-level discussion**

M, efSearch, efConstruction, memory vs IVF.
### Q4. Backup story?

**Expected answer (junior)**

Backup documents + embeddings config; vector index snapshots optional because we can rebuild. Test a restore.

**Common mistakes**

We take Docker volumes sometimes.

**Senior-level discussion**

RPO/RTO, rebuild time SLOs.
### Q5. Why Chroma in tutorials and not in your design?

**Expected answer (junior)**

Fast learning loop. For prod I need backups, HA, filters at scale — maybe Qdrant/pgvector.

**Common mistakes**

Chroma is fake.

**Senior-level discussion**

Embedded vs client-server Chroma, and when it is actually enough.


---

## Whiteboard prompts

- Architecture: FastAPI, Postgres, Qdrant. Where is the source of truth?
- Tenant filter forgotten — draw the leak and the test.
- Estimate RAM: 10M vectors × 768-d float32 + HNSW overhead ~1.5–2x.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for tradeoffs and tenancy, not memorized vendor feature lists.
