# Design: chat over 50k internal docs

**Clarify:** employees only? languages? PDF+wiki? p95? citations required? regulated?

**Happy path:** ingest pipeline, hybrid retrieve, rerank, generate with citations, abstain.

**Scale:** 50k docs × ~20 chunks = ~1M vectors. pgvector or Qdrant. RAM estimate.

**Eval:** 100 gold questions, CI gate.

**Security:** SSO, ACLs on docs → filters, injection from wiki.

**Week 1 vs month 6:** naive RAG → hybrid+rerank+evals → ACLs+traces.

**Poke:** "Legal wants an audit." Store prompt version, doc version, who asked, retrieved ids.
