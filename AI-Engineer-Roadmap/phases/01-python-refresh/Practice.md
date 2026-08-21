# Practice — Phase 1: Python refresh

Guided drills. Timer on. No tutorial hopping.



### Drill 1. Type this function

Take an untyped function from an old notebook. Add hints until pyright is quiet.

**Done when:** No `Any` unless you can justify it.

### Drill 2. Sleep is not async

Write two versions of a 1-second fake I/O burst of 10 calls: sync `time.sleep` vs `asyncio.gather` + `asyncio.sleep`. Time both.

**Done when:** You can explain why gather is ~1s and sync is ~10s.

### Drill 3. with-statement

Write a context manager that times a block and prints milliseconds.

**Done when:** Works with exceptions inside the block.

## Cool-down

Explain today's idea to a rubber duck in 90 seconds using the analogy from Theory.md. If you need the file open, you are not done.
