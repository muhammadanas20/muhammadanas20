# Flashcards — Phase 1: Python refresh

Say the answer. Then open. Do the deck two days later. That is the whole spaced-repetition system.

**Q1.** What does await do?

<details><summary>Answer</summary>

Pauses the coroutine until the awaitable finishes, letting the loop run other work.

</details>

**Q2.** When is async the wrong tool?

<details><summary>Answer</summary>

CPU-bound work; tiny scripts; libraries that are sync-only without a thread.

</details>

**Q3.** Why pydantic over json.loads?

<details><summary>Answer</summary>

Types, constraints, useful errors.

</details>

**Q4.** What is jitter in retries?

<details><summary>Answer</summary>

Random extra delay so clients desynchronize.

</details>

**Q5.** sync vs async sleep?

<details><summary>Answer</summary>

time.sleep blocks the thread/loop; asyncio.sleep yields.

</details>

**Q6.** Protocol vs ABC?

<details><summary>Answer</summary>

Protocol is structural typing (has the methods); ABC is nominal inheritance.

</details>

**Q7.** What is an async generator?

<details><summary>Answer</summary>

async def with yield; iterate with async for.

</details>

**Q8.** Why frozen dataclass for settings?

<details><summary>Answer</summary>

Immutability, fewer accidental writes.

</details>

**Q9.** What is structured concurrency?

<details><summary>Answer</summary>

TaskGroup/nursery: child tasks finish or cancel together.

</details>

**Q10.** Name a transient HTTP code.

<details><summary>Answer</summary>

429, 502, 503, 504.

</details>
