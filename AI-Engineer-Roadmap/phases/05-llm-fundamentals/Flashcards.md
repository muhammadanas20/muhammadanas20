# Flashcards — Phase 5: LLM fundamentals

Say the answer. Then open. Do the deck two days later. That is the whole spaced-repetition system.

**Q1.** What is a token?

<details><summary>Answer</summary>

A chunk of text the tokenizer emits; billing and limits use it.

</details>

**Q2.** Why temp 0 for extraction?

<details><summary>Answer</summary>

Less sampling noise, more stable JSON.

</details>

**Q3.** Does the model know your docs?

<details><summary>Answer</summary>

Not unless they were in training (stale/public) or you send/retrieve them.

</details>

**Q4.** What is a tool call?

<details><summary>Answer</summary>

Structured request from the model for you to run a function.

</details>

**Q5.** Why pydantic after JSON mode?

<details><summary>Answer</summary>

Wrong types/values, extra fields, provider bugs.

</details>

**Q6.** Context vs memory?

<details><summary>Answer</summary>

Context is this request's desk; memory is your DB.

</details>

**Q7.** Name three roles.

<details><summary>Answer</summary>

system, user, assistant (plus tool).

</details>

**Q8.** RAG vs fine-tune in one line?

<details><summary>Answer</summary>

RAG for facts; fine-tune for style/skill.

</details>

**Q9.** What is TTFT?

<details><summary>Answer</summary>

Time to first token.

</details>

**Q10.** Why cap max_tokens?

<details><summary>Answer</summary>

Cost and runaway generations.

</details>
