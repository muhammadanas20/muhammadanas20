# Interview — Phase 6: Embeddings and search

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. What is an embedding?

**Expected answer (junior)**

A vector such that similar meanings are close. Produced by an embedding model, not by a chat model (usually).

**Common mistakes**

Calling ChatGPT 'the embedding'. Confusing tokens with vectors.

**Senior-level discussion**

MTEB, domain shift, dim vs quality, late interaction models.
### Q2. How do you chunk a messy PDF?

**Expected answer (junior)**

Extract structure if possible; split by headings/pages as fallback; keep tables; overlap; store page numbers.

**Common mistakes**

500-char slices. OCR ignored.

**Senior-level discussion**

Layout models, parent-child, multimodal embeddings for figures.
### Q3. Cosine or L2?

**Expected answer (junior)**

Cosine for text when we care about orientation. If the vendor says normalize + dot, do that.

**Common mistakes**

Random choice.

**Senior-level discussion**

Inner product indexes, metric must match the index.
### Q4. How do you know retrieval works without an LLM?

**Expected answer (junior)**

Gold queries, recall@k, MRR, looking at the actual chunks.

**Common mistakes**

Only vibe-checking the chatbot.

**Senior-level discussion**

nDCG, contamination, inter-annotator agreement.
### Q5. Hybrid search in one minute.

**Expected answer (junior)**

Keyword (BM25) plus dense vectors, fuse scores, often then rerank.

**Common mistakes**

Hybrid means two vector DBs.

**Senior-level discussion**

RRF, learned fusion, query routing.


---

## Whiteboard prompts

- Draw ingest vs query paths. Mark the model id.
- Given a 20-page PDF with 3 tables, sketch chunks.
- Estimate RAM for 1M chunks × 768-d float32.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for chunking quality and same-model discipline, not vendor names.
