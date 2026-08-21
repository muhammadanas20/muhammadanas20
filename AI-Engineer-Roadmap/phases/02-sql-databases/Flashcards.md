# Flashcards — Phase 2: SQL, Postgres, and Redis

Say the answer. Then open. Do the deck two days later. That is the whole spaced-repetition system.

**Q1.** Source of truth for chats?

<details><summary>Answer</summary>

Postgres (or similar RDBMS).

</details>

**Q2.** Redis use cases in AI apps?

<details><summary>Answer</summary>

Rate limit, cache, session, job queue, pub/sub.

</details>

**Q3.** What does EXPLAIN tell you?

<details><summary>Answer</summary>

The query plan: scans, joins, estimated cost.

</details>

**Q4.** Foreign key purpose?

<details><summary>Answer</summary>

The DB enforces that referenced rows exist.

</details>

**Q5.** Why UUID PKs?

<details><summary>Answer</summary>

Not guessable, merge-friendly, can generate in app.

</details>

**Q6.** Cache stampede?

<details><summary>Answer</summary>

Many requests miss cache together and slam the origin.

</details>

**Q7.** Parameterized SQL?

<details><summary>Answer</summary>

Placeholders + bound values, never string concat.

</details>

**Q8.** Connection pool why?

<details><summary>Answer</summary>

Creating PG connections is expensive.

</details>

**Q9.** Soft delete?

<details><summary>Answer</summary>

Set deleted_at instead of removing the row.

</details>

**Q10.** When pgvector?

<details><summary>Answer</summary>

You already run Postgres and vector scale is moderate.

</details>
