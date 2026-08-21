# Phase 4 — Docker

<p>
  <img alt="difficulty" src="https://img.shields.io/badge/difficulty-Medium-blue">
  <img alt="time" src="https://img.shields.io/badge/time-5-7%20days-green">
  <img alt="phase" src="https://img.shields.io/badge/phase-4-8b5cf6">
</p>

**Estimated time:** 5-7 days  
**Difficulty:** Medium  
**Exit ticket:** `docker compose up` runs the Phase 3 API with Postgres and Redis.

If it only runs on your laptop, it does not run.

## Learning objectives

When this phase is done you can:

- Write a Dockerfile with a non-root user and a slim base image.
- Explain layers, cache, and why COPY order matters.
- Use Compose for app + Postgres + Redis.
- Mount volumes and attach networks on purpose.
- Add healthchecks and a .dockerignore.

## Prerequisites

- Phase 0 Docker installed. Phase 3 app exists or use the stub in code/.

## Topics

- Images
- layers
- Compose
- volumes
- networks
- healthchecks
- multi-stage

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

[Home](../../README.md) · Prev: [Phase 3](../03-fastapi/) · Next: [Phase 5 · LLMs](../05-llm-fundamentals/)

## Time box

If you are on the 90-day plan, finish this phase in the window on [90_DAY_PLAN.md](../../90_DAY_PLAN.md).  
If you are on the 180-day plan, use [WEEKLY_PLAN.md](../../WEEKLY_PLAN.md).

Do not collect frameworks. Collect **exit tickets**.
