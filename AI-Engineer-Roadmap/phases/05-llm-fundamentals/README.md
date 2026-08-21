# Phase 5 — LLM fundamentals

<p>
  <img alt="difficulty" src="https://img.shields.io/badge/difficulty-Medium-blue">
  <img alt="time" src="https://img.shields.io/badge/time-10-14%20days-green">
  <img alt="phase" src="https://img.shields.io/badge/phase-5-8b5cf6">
</p>

**Estimated time:** 10-14 days  
**Difficulty:** Medium  
**Exit ticket:** A client that streams, validates JSON with Pydantic, and performs one tool call.

Treat the model as a component: tokens, context, temperature, tools, structured output, streaming.

## Learning objectives

When this phase is done you can:

- Explain transformers at a picture level (no need to derive backprop).
- Count tokens and relate them to cost and context limits.
- Control temperature, top-p, and stop sequences with intent.
- Write prompts that are versioned, testable, and not folklore.
- Use tool/function calling and structured outputs.
- Stream tokens and cancel.

## Prerequisites

- Phases 0–4. You can ship a FastAPI service in Docker.

## Topics

- Transformers (intuition)
- Tokens and context windows
- Embeddings intro
- Temperature / sampling
- Prompt engineering
- Tool calling
- Structured outputs
- Streaming

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

[Home](../../README.md) · Prev: [Phase 4](../04-docker/) · Next: [Phase 6 · Embeddings](../06-embeddings-search/)

## Time box

If you are on the 90-day plan, finish this phase in the window on [90_DAY_PLAN.md](../../90_DAY_PLAN.md).  
If you are on the 180-day plan, use [WEEKLY_PLAN.md](../../WEEKLY_PLAN.md).

Do not collect frameworks. Collect **exit tickets**.
