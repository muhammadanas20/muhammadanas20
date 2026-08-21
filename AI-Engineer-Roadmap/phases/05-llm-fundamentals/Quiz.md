# Quiz — Phase 5: LLM fundamentals

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

1. An LLM fundamentally:
    A) Queries Google
    B) Predicts next tokens
    C) Stores your PDFs in weights by default
    D) Guarantees truth
2. A token is:
    A) Always one English word
    B) A model-specific text piece
    C) A Docker layer
    D) A JWT
3. Temperature 0 is best for:
    A) Poetry
    B) JSON extraction
    C) Diversity of jokes
    D) Training
4. Context window is:
    A) Infinite memory
    B) A finite token budget for the prompt+response
    C) RAM of the GPU only
    D) Your Postgres size
5. Tool calling means:
    A) The model SSHs into prod
    B) The model proposes a structured function call that YOUR code runs
    C) Fine-tuning
    D) Embeddings
6. JSON mode guarantees:
    A) Correct business values
    B) Mostly valid JSON shape (still validate)
    C) Citations
    D) Low cost
7. Lost in the middle means:
    A) GPUs overheat
    B) Models use mid-context worse than edges
    C) Redis TTL
    D) Docker layers
8. Fine-tune to store a weekly-changing policy?
    A) Yes always
    B) No — use RAG / retrieval
    C) Yes with temperature 2
    D) Use Redis only
9. Streaming helps:
    A) TTFT UX and cancellation
    B) Accuracy always
    C) Token prices
    D) SQL
10. System prompt is:
    A) A secret key
    B) High-level instructions for the model
    C) A vector DB
    D) A healthcheck

---

<details>
<summary>Answers (spoiler)</summary>

1. **B** — Next-token prediction.
2. **B** — Tokenizer dependent.
3. **B** — Low variance.
4. **B** — Finite.
5. **B** — You dispatch.
6. **B** — Shape ≠ truth.
7. **B** — Liu et al.
8. **B** — Facts that change → retrieve.
9. **A** — UX.
10. **B** — Handbook.

</details>
