# FAQ — Phase 6: Embeddings and search

### Chat model as embedder?

Some APIs offer it. Dedicated embedding models are cheaper and usually better for kNN. Don't roll your own by averaging chat hidden states unless you know why.

### GPU needed?

No for small corpora. CPU sentence-transformers is fine for this phase.

### PDF libraries?

pypdf for simple; pymupdf / unstructured / vendor OCR for real documents.

Didn't see your question? Open an issue. Beginner questions are first-class.
