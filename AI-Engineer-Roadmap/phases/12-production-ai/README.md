# Phase 12 — Production AI / LLMOps

<p>
  <img alt="difficulty" src="https://img.shields.io/badge/difficulty-Hard-blue">
  <img alt="time" src="https://img.shields.io/badge/time-10-14%20days-green">
  <img alt="phase" src="https://img.shields.io/badge/phase-12-8b5cf6">
</p>

**Estimated time:** 10-14 days  
**Difficulty:** Hard  
**Exit ticket:** Traces on every request, an eval gate in CI, cache, rate limit, and a fallback model.

If you cannot trace it, cache it, evaluate it, or fall back, you do not operate it.

## Learning objectives

When this phase is done you can:

- Add tracing (OpenTelemetry / Langfuse / LangSmith).
- Run offline evals (Ragas, DeepEval, Promptfoo) in CI.
- Cache embeddings and safe answers.
- Rate limit and budget tokens.
- Route and fall back across models.

## Prerequisites

- A deployed or local RAG/chat app. Phase 8 evals started.

## Topics

- Monitoring
- tracing
- Langfuse
- LangSmith
- Promptfoo
- DeepEval
- Ragas
- caching
- rate limits
- fallback
- routing

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

[Home](../../README.md) · Prev: [Phase 11](../11-deployment/) · Next: [Phase 13 · Security](../13-security/)

## Time box

If you are on the 90-day plan, finish this phase in the window on [90_DAY_PLAN.md](../../90_DAY_PLAN.md).  
If you are on the 180-day plan, use [WEEKLY_PLAN.md](../../WEEKLY_PLAN.md).

Do not collect frameworks. Collect **exit tickets**.
