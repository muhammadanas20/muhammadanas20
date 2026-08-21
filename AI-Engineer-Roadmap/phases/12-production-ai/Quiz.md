# Quiz — Phase 12: Production AI / LLMOps

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

1. 200 OK implies
    A) Correct answer
    B) HTTP succeeded, not truth
    C) Faithfulness 1.0
    D) Cheap
2. A trace is
    A) A stack of spans for one request
    B) A Docker image
    C) A JWT
    D) A vector
3. Semantic cache danger
    A) It's slow
    B) Stale or cross-tenant answers
    C) It uses Redis
    D) It needs Docker
4. Pin model versions because
    A) Aliases can drift
    B) It is prettier
    C) CI forbids dates
    D) Cosine
5. Fallback is for
    A) Happy path only
    B) Timeouts/429/5xx/parse fail
    C) CSS
    D) Embeddings dim
6. LLM-as-judge risk
    A) Bias and cost
    B) It never works
    C) Illegal always
    D) Needs k8s
7. Rate limit unit for LLMs
    A) Preferably tokens/tenant
    B) Only CPU
    C) Only IP always
    D) GPU clocks
8. Promptfoo is
    A) A GPU
    B) An eval/regression tool
    C) A vector DB
    D) Nginx
9. Cache key must include
    A) Tenant + prompt/model/doc version as needed
    B) Only the question text ever
    C) The user's password
    D) Nothing
10. Eval in CI should
    A) Fail the build on large regressions
    B) Only run on your laptop
    C) Edit gold labels until green
    D) Use production PII

---

<details>
<summary>Answers (spoiler)</summary>

1. **B** — Quality ≠ status.
2. **A** — Recorder.
3. **B** — Correctness.
4. **A** — Drift.
5. **B** — Degrade.
6. **A** — Use carefully.
7. **A** — Tokens.
8. **B** — Evals.
9. **A** — Isolation.
10. **A** — Gate.

</details>
