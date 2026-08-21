# Interview — Phase 8: Retrieval-Augmented Generation (RAG)

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. Draw RAG on the board.

**Expected answer (junior)**

Ingest: load-chunk-embed-store. Query: rewrite-retrieve-filter-rerank-prompt-generate-cite. Eval loop.

**Common mistakes**

Starting with LangChain classes.

**Senior-level discussion**

Where you'd put cache, tenancy, tracing.
### Q2. RAG still hallucinated. Debug.

**Expected answer (junior)**

Print retrieved chunks. Check they actually support the answer. If yes, prompt/grounding issue. If no, retrieval/chunking. Check filters, query rewrite, k.

**Common mistakes**

Buy a bigger model immediately.

**Senior-level discussion**

Faithfulness metrics, injection, stale index.
### Q3. Hybrid vs dense-only?

**Expected answer (junior)**

Keywords catch ids/codes; dense catches paraphrases. Fuse with RRF. Measure.

**Common mistakes**

Hybrid is always better so skip eval.

**Senior-level discussion**

When BM25 dominates (legal clauses) vs semantic FAQs.
### Q4. How do you evaluate RAG?

**Expected answer (junior)**

Gold questions, retrieval recall@k, faithfulness, relevancy, human spot checks, later online thumbs. Freeze the set.

**Common mistakes**

We ask the LLM if it did a good job (only).

**Senior-level discussion**

LLM-as-judge bias, DeepEval/Ragas pitfalls, inter-annotator.
### Q5. When is an agent better than RAG?

**Expected answer (junior)**

When you need tools, multi-step, or multiple sources with decisions. Not for 'search these docs and answer'.

**Common mistakes**

Agents always; RAG is dead.

**Senior-level discussion**

Cost/latency, failure modes, mixing agentic RAG.


---

## Whiteboard prompts

- Full RAG architecture for a 10k-doc help center, 500 QPS peak, 2s p95.
- Compare naive vs hybrid+rerank vs GraphRAG for 'What is our refund policy?' vs 'Themes in 10k tickets'.
- Design an eval harness with CI gate.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for whether you debug retrieval before blaming the LLM, and whether you have numbers.
