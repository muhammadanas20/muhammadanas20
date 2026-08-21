# Phase 2 — SQL, Postgres, and Redis

<p>
  <img alt="difficulty" src="https://img.shields.io/badge/difficulty-Medium-blue">
  <img alt="time" src="https://img.shields.io/badge/time-7-10%20days-green">
  <img alt="phase" src="https://img.shields.io/badge/phase-2-8b5cf6">
</p>

**Estimated time:** 7-10 days  
**Difficulty:** Medium  
**Exit ticket:** Migrated Postgres schema for users/docs/chats plus a Redis rate limiter.

Chat history, users, documents, and rate limits do not belong in a JSON file.

## Learning objectives

When this phase is done you can:

- Model users, documents, conversations, and messages in SQL.
- Use Postgres indexes, JSONB, and EXPLAIN without fear.
- Run schema migrations (Alembic or similar).
- Use Redis for cache, rate limits, and short-lived session data.
- Know when SQL vs a vector DB vs object storage is the right store.

## Prerequisites

- Phase 0–1. You can write Python and run Docker.

## Topics

- SQL
- Postgres
- indexes
- JSONB
- migrations
- Redis
- caching
- rate limits

## How to move through this phase

1. Read `Theory.md` once without coding.
2. Type every example in `Examples.md`. Change one number. Predict the new output.
3. Do `Practice.md`, then exercises in order (B → M → H).
4. Take `Quiz.md` cold. If you score under 80%, re-read, do not proceed.
5. Answer `Interview.md` **out loud**.
6. Ship `MiniProject.md` to your GitHub.
7. Skim `ProductionTips.md` and `CommonMistakes.md` before you call it done.

## Files in this folder

| File | Role |
| --- | --- |
| [Theory.md](./Theory.md) | Full lesson (all 25 sections) |
| [Examples.md](./Examples.md) | Commented code, dry runs, complexity |
| [Practice.md](./Practice.md) | Guided drills |
| [Exercises.md](./Exercises.md) | Beginner / medium / hard |
| [Assignments.md](./Assignments.md) | Take-home style |
| [Quiz.md](./Quiz.md) | Self-check |
| [Flashcards.md](./Flashcards.md) | Spaced repetition |
| [Interview.md](./Interview.md) | Questions, answers, senior discussion |
| [Cheatsheet.md](./Cheatsheet.md) | One-pager |
| [MiniProject.md](./MiniProject.md) | Portfolio piece |
| [Resources.md](./Resources.md) | Docs, papers |
| [FAQ.md](./FAQ.md) | Junior questions |
| [Debugging.md](./Debugging.md) | Broken code |
| [CommonMistakes.md](./CommonMistakes.md) | Code-review scars |
| [ProductionTips.md](./ProductionTips.md) | Cost, latency, reliability |
| [Challenge.md](./Challenge.md) | Stretch |
| [Solutions.md](./Solutions.md) | Spoilers |

Runnable snippets: [`code/`](./code/)

## Navigation

[Home](../../README.md) · Prev: [Phase 1](../01-python-refresh/) · Next: [Phase 3 · FastAPI](../03-fastapi/)

## Time box

If you are on the 90-day plan, finish this phase in the window on [90_DAY_PLAN.md](../../90_DAY_PLAN.md).  
If you are on the 180-day plan, use [WEEKLY_PLAN.md](../../WEEKLY_PLAN.md).

Do not collect frameworks. Collect **exit tickets**.
