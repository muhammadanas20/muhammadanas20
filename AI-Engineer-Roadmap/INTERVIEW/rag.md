# RAG interview extras

**Q. MMR?**  
Maximal marginal relevance — trade relevance for diversity so 5 chunks aren't paraphrases of one paragraph.

**Q. Contextual retrieval (Anthropic-style)?**  
Prepend headings / document context to chunks before embedding so they aren't orphans.

**Q. How do you handle recency?**  
Metadata filter on date, recency boost, or re-index. Don't assume embeddings know "yesterday."

**Q. Multi-hop questions?**  
Maybe agentic RAG or query decomposition. Measure against naive — many "multi-hop" questions are just bad chunks.

**Q. Eval contamination?**  
Don't tune prompts on the only gold set. Holdout. Don't generate gold questions solely from the same LLM you evaluate.
