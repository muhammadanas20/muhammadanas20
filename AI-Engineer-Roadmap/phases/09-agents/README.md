# Phase 9 — Agents

<p>
  <img alt="difficulty" src="https://img.shields.io/badge/difficulty-Hard-blue">
  <img alt="time" src="https://img.shields.io/badge/time-14-21%20days-green">
  <img alt="phase" src="https://img.shields.io/badge/phase-9-8b5cf6">
</p>

**Estimated time:** 14-21 days  
**Difficulty:** Hard  
**Exit ticket:** An agent that queries SQL safely, logs every tool call, and cannot DROP TABLE.

Multi-step work with tools. Also: when an agent is the wrong idea.

## Learning objectives

When this phase is done you can:

- Write a tool loop with no framework.
- Add max steps, timeouts, and allow-listed tools.
- Compare LangGraph, PydanticAI, CrewAI, OpenAI Agents SDK honestly.
- Implement memory that is not 'stuff the whole chat into the prompt'.
- Know planning vs reacting vs graph state machines.

## Prerequisites

- Phases 5 and 8. FastAPI + SQL strongly recommended.

## Topics

- Tool calling
- LangGraph
- PydanticAI
- CrewAI
- OpenAI Agents SDK
- Memory
- Planning
- Reflection

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

[Home](../../README.md) · Prev: [Phase 8](../08-rag/) · Next: [Phase 10 · MCP](../10-mcp/)

## Time box

If you are on the 90-day plan, finish this phase in the window on [90_DAY_PLAN.md](../../90_DAY_PLAN.md).  
If you are on the 180-day plan, use [WEEKLY_PLAN.md](../../WEEKLY_PLAN.md).

Do not collect frameworks. Collect **exit tickets**.
