# Flashcards — Phase 3: FastAPI

Say the answer. Then open. Do the deck two days later. That is the whole spaced-repetition system.

**Q1.** Name 2xx, 4xx, 5xx.

<details><summary>Answer</summary>

Success, client error, server error.

</details>

**Q2.** What is OpenAPI here?

<details><summary>Answer</summary>

The auto-generated contract of your API.

</details>

**Q3.** Bearer token lives in?

<details><summary>Answer</summary>

Authorization header.

</details>

**Q4.** Why request IDs?

<details><summary>Answer</summary>

Tie logs, traces, and user reports together.

</details>

**Q5.** Health vs ready?

<details><summary>Answer</summary>

Health: process up. Ready: dependencies reachable.

</details>

**Q6.** SSE content type?

<details><summary>Answer</summary>

text/event-stream.

</details>

**Q7.** Why not uvicorn --reload in prod?

<details><summary>Answer</summary>

Extra process, file watchers, not a process manager.

</details>

**Q8.** 422 in FastAPI?

<details><summary>Answer</summary>

Validation error from pydantic.

</details>

**Q9.** Idempotency key?

<details><summary>Answer</summary>

Client token so retries do not double-create.

</details>

**Q10.** Where to put JWT secret?

<details><summary>Answer</summary>

Environment / secret manager, never source.

</details>
