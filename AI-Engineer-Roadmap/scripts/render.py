"""Markdown renderers for phase lesson files.

Keep this module boring. Content lives in the phase data modules.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any


def _join(items: list[str], numbered: bool = False) -> str:
    if numbered:
        return "\n".join(f"{i}. {t}" for i, t in enumerate(items, 1))
    return "\n".join(f"- {t}" for t in items)


def readme(p: dict[str, Any]) -> str:
    objs = _join(p["objectives"])
    prereq = _join(p["prerequisites"])
    topics = _join(p["topics"])
    nav = p["nav"]
    return f"""# Phase {p["num"]} — {p["title"]}

<p>
  <img alt="difficulty" src="https://img.shields.io/badge/difficulty-{p["difficulty"]}-blue">
  <img alt="time" src="https://img.shields.io/badge/time-{p["hours"].replace(" ", "%20")}-green">
  <img alt="phase" src="https://img.shields.io/badge/phase-{p["num"]}-8b5cf6">
</p>

**Estimated time:** {p["hours"]}  
**Difficulty:** {p["difficulty"]}  
**Exit ticket:** {p["exit_ticket"]}

{p["tagline"]}

## Learning objectives

When this phase is done you can:

{objs}

## Prerequisites

{prereq}

## Topics

{topics}

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

{nav}

## Time box

If you are on the 90-day plan, finish this phase in the window on [90_DAY_PLAN.md](../../90_DAY_PLAN.md).  
If you are on the 180-day plan, use [WEEKLY_PLAN.md](../../WEEKLY_PLAN.md).

Do not collect frameworks. Collect **exit tickets**.
"""


def theory(p: dict[str, Any]) -> str:
    t = p["theory"]
    return f"""# Theory — Phase {p["num"]}: {p["title"]}

> Read this before any code. If a word is new, we define it before we use it.

## Table of contents

1. [Introduction](#1-introduction)
2. [Why this exists](#2-why-this-exists)
3. [Real-world analogy](#3-real-world-analogy)
4. [Visual diagram](#4-visual-diagram)
5. [Architecture diagram](#5-architecture-diagram)
6. [Beginner explanation](#6-beginner-explanation)
7. [Intermediate explanation](#7-intermediate-explanation)
8. [Advanced explanation](#8-advanced-explanation)
9. [Production explanation](#9-production-explanation)
10. [Code examples](#10-code-examples)
11. [Beginner exercises](#11-beginner-exercises)
12. [Medium exercises](#12-medium-exercises)
13. [Hard exercises](#13-hard-exercises)
14. [Project](#14-project)
15. [Interview questions](#15-interview-questions)
16. [Flashcards](#16-flashcards)
17. [Quiz](#17-quiz)
18. [Common mistakes](#18-common-mistakes)
19. [Debugging examples](#19-debugging-examples)
20. [Best practices](#20-best-practices)
21. [Industry standards](#21-industry-standards)
22. [Performance tips](#22-performance-tips)
23. [Security considerations](#23-security-considerations)
24. [References](#24-references)
25. [Further reading](#25-further-reading)

---

## 1. Introduction

{t["intro"]}

**In one sentence:** {t["one_liner"]}

## 2. Why this exists

{t["why"]}

If this phase did not exist, {t["if_missing"]}

## 3. Real-world analogy

{t["analogy"]}

Keep this picture in your head when the jargon starts.

## 4. Visual diagram

{t["visual"]}

## 5. Architecture diagram

{t["architecture"]}

## 6. Beginner explanation

{t["beginner"]}

## 7. Intermediate explanation

{t["intermediate"]}

## 8. Advanced explanation

{t["advanced"]}

## 9. Production explanation

{t["production"]}

**When to use:** {t["when"]}

**When not to use:** {t["when_not"]}

## 10. Code examples

Full walkthroughs with dry runs live in [Examples.md](./Examples.md) and [`code/`](./code/).

Preview:

```python
{t["code_preview"]}
```

What to notice:

{t["code_notes"]}

## 11. Beginner exercises

{t["ex_b"]}

Details: [Exercises.md](./Exercises.md)

## 12. Medium exercises

{t["ex_m"]}

## 13. Hard exercises

{t["ex_h"]}

## 14. Project

{t["project"]}

Spec: [MiniProject.md](./MiniProject.md)

## 15. Interview questions

{t["interview_preview"]}

The full bank with expected answers, common mistakes, senior discussion, and whiteboard prompts: [Interview.md](./Interview.md)

## 16. Flashcards

Use [Flashcards.md](./Flashcards.md). Say the answer out loud before you flip.

Sample:

{t["flash_sample"]}

## 17. Quiz

Take [Quiz.md](./Quiz.md) cold. Passing bar: 80%.

## 18. Common mistakes

{t["mistakes_preview"]}

More: [CommonMistakes.md](./CommonMistakes.md)

## 19. Debugging examples

{t["debug_preview"]}

Playgrounds: [Debugging.md](./Debugging.md)

## 20. Best practices

{t["best"]}

## 21. Industry standards

{t["industry"]}

## 22. Performance tips

{t["perf"]}

## 23. Security considerations

{t["security"]}

## 24. References

{t["refs"]}

## 25. Further reading

{t["further"]}

---

Next: type the code in [Examples.md](./Examples.md). Reading is not the skill. Running it is.
"""


def examples(p: dict[str, Any]) -> str:
    blocks = []
    for i, ex in enumerate(p["examples"], 1):
        blocks.append(
            f"""### Example {i}. {ex["title"]}

{ex["why"]}

```python
{ex["code"]}
```

**What every interesting line is doing**

{ex["line_by_line"]}

**Expected output**

```text
{ex["output"]}
```

**Dry run**

{ex["dry_run"]}

**Memory**

{ex["memory"]}

**Time complexity:** {ex["time"]}  
**Space complexity:** {ex["space"]}

**Alternatives**

{ex["alternatives"]}

**Optimization**

{ex["optimization"]}
"""
        )
    body = "\n---\n\n".join(blocks)
    return f"""# Examples — Phase {p["num"]}: {p["title"]}

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).

{p.get("examples_intro", "")}

---

{body}

---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
"""


def practice(p: dict[str, Any]) -> str:
    drills = "\n\n".join(
        f"### Drill {i}. {d['title']}\n\n{d['body']}\n\n**Done when:** {d['done']}"
        for i, d in enumerate(p["practice"], 1)
    )
    return f"""# Practice — Phase {p["num"]}: {p["title"]}

Guided drills. Timer on. No tutorial hopping.

{p.get("practice_intro", "")}

{drills}

## Cool-down

Explain today's idea to a rubber duck in 90 seconds using the analogy from Theory.md. If you need the file open, you are not done.
"""


def exercises(p: dict[str, Any]) -> str:
    def sec(level: str, items: list[dict[str, str]]) -> str:
        parts = []
        for i, it in enumerate(items, 1):
            parts.append(f"### {level[0].upper()}{i}. {it['title']}\n\n{it['body']}\n\n**Constraints:** {it['constraints']}")
        return "\n\n".join(parts)

    return f"""# Exercises — Phase {p["num"]}: {p["title"]}

Do them in order. Hard exercises assume the medium ones exist in your repo.

Hints are in [Solutions.md](./Solutions.md). Use them after 25 minutes of being stuck, not after 25 seconds.

## Beginner

{sec("beginner", p["exercises"]["beginner"])}

## Medium

{sec("medium", p["exercises"]["medium"])}

## Hard

{sec("hard", p["exercises"]["hard"])}

## Submission shape

Each exercise gets a folder:

```text
exercises/phase{p["num"]}/eN/
  README.md
  main.py
  test_main.py
```

Your `README.md` must include: approach, complexity, what you would do in production.
"""


def assignments(p: dict[str, Any]) -> str:
    items = []
    for i, a in enumerate(p["assignments"], 1):
        rubric = _join(a["rubric"])
        items.append(
            f"""## Assignment {i}. {a["title"]}

**Time box:** {a["time"]}

{a["brief"]}

### Deliverables

{_join(a["deliverables"])}

### Rubric

{rubric}
"""
        )
    return f"""# Assignments — Phase {p["num"]}: {p["title"]}

These mimic take-homes. Time-box them. A finished 80% with a README beats an infinite 99%.

{"".join(items)}

## Academic integrity

You may use an assistant. You must be able to delete `main.py` and rewrite it from memory the next morning. Interviews will ask you to.
"""


def quiz(p: dict[str, Any]) -> str:
    qs = []
    ans = []
    for i, q in enumerate(p["quiz"], 1):
        opts = "\n".join(f"    {k}) {v}" for k, v in q["choices"].items())
        qs.append(f"{i}. {q['q']}\n{opts}")
        ans.append(f"{i}. **{q['answer']}** — {q['explain']}")
    return f"""# Quiz — Phase {p["num"]}: {p["title"]}

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

{chr(10).join(qs)}

---

<details>
<summary>Answers (spoiler)</summary>

{chr(10).join(ans)}

</details>
"""


def flashcards(p: dict[str, Any]) -> str:
    cards = "\n\n".join(
        f"**Q{i}.** {c['q']}\n\n<details><summary>Answer</summary>\n\n{c['a']}\n\n</details>"
        for i, c in enumerate(p["flashcards"], 1)
    )
    return f"""# Flashcards — Phase {p["num"]}: {p["title"]}

Say the answer. Then open. Do the deck two days later. That is the whole spaced-repetition system.

{cards}
"""


def interview(p: dict[str, Any]) -> str:
    bank = []
    for i, q in enumerate(p["interview"], 1):
        bank.append(
            f"""### Q{i}. {q["q"]}

**Expected answer (junior)**

{q["junior"]}

**Common mistakes**

{q["mistakes"]}

**Senior-level discussion**

{q["senior"]}
"""
        )
    wb = "\n".join(f"- {w}" for w in p["whiteboard"])
    return f"""# Interview — Phase {p["num"]}: {p["title"]}

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

{"".join(bank)}

---

## Whiteboard prompts

{wb}

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for {p["interview_listen"]}.
"""


def cheatsheet(p: dict[str, Any]) -> str:
    return f"""# Cheatsheet — Phase {p["num"]}: {p["title"]}

Print or pin. This is not a substitute for Theory.md.

## Remember

{p["cheatsheet"]["remember"]}

## Commands / snippets

```bash
{p["cheatsheet"]["bash"]}
```

```python
{p["cheatsheet"]["python"]}
```

## Decision tree

{p["cheatsheet"]["decisions"]}

## Numbers

{p["cheatsheet"]["numbers"]}

## Do not

{p["cheatsheet"]["do_not"]}
"""


def miniproject(p: dict[str, Any]) -> str:
    m = p["miniproject"]
    return f"""# Mini-project — Phase {p["num"]}: {p["title"]}

**Name:** {m["name"]}  
**Time box:** {m["time"]}  
**Difficulty:** {m["difficulty"]}

## Why this project

{m["why"]}

## User story

{m["story"]}

## Requirements

Must:

{_join(m["must"])}

Should:

{_join(m["should"])}

Won't (this week):

{_join(m["wont"])}

## Architecture

{m["architecture"]}

## Suggested layout

```text
{m["layout"]}
```

## Rubric

{_join(m["rubric"])}

## Stretch

{m["stretch"]}

When it works, write the README as if a hiring manager will open it on their phone. Then add a resume bullet using [RESUME_GUIDE.md](../../RESUME_GUIDE.md).
"""


def resources(p: dict[str, Any]) -> str:
    official = "\n".join(f"- {x}" for x in p["resources"]["official"])
    extra = "\n".join(f"- {x}" for x in p["resources"]["extra"])
    papers = "\n".join(f"- {x}" for x in p["resources"]["papers"])
    return f"""# Resources — Phase {p["num"]}: {p["title"]}

Official first. Then one extra. Then stop.

## Official

{official}

## Extra (pick one)

{extra}

## Papers / deep dives

{papers}

## How to read

1. Skim headings.
2. Recreate one diagram from memory.
3. Implement the smallest example.
4. Come back only if stuck.

More tabs are not more learning. See also the global [RESOURCES.md](../../RESOURCES.md).
"""


def faq(p: dict[str, Any]) -> str:
    items = "\n\n".join(f"### {f['q']}\n\n{f['a']}" for f in p["faq"])
    return f"""# FAQ — Phase {p["num"]}: {p["title"]}

{items}

Didn't see your question? Open an issue. Beginner questions are first-class.
"""


def debugging(p: dict[str, Any]) -> str:
    items = []
    for i, d in enumerate(p["debugging"], 1):
        items.append(
            f"""## Bug {i}. {d["title"]}

**Symptom**

{d["symptom"]}

**Broken mental model**

{d["wrong"]}

**How to see it**

{d["see"]}

**Fix**

{d["fix"]}

**Prevention**

{d["prevent"]}
"""
        )
    return f"""# Debugging — Phase {p["num"]}: {p["title"]}

Debugging is the job. These are bugs we see every week.

{"".join(items)}

## A ritual that works

1. Reproduce in the smallest script.
2. Print types and shapes (or tokens, or status codes).
3. Bisect: last working commit vs now.
4. Read the error from the bottom.
5. Write a test so it cannot return.
"""


def common_mistakes(p: dict[str, Any]) -> str:
    items = "\n\n".join(
        f"### {i}. {m['title']}\n\n{m['body']}\n\n**Do this instead:** {m['instead']}"
        for i, m in enumerate(p["mistakes"], 1)
    )
    return f"""# Common mistakes — Phase {p["num"]}: {p["title"]}

{items}

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
"""


def production_tips(p: dict[str, Any]) -> str:
    t = p["prod_tips"]
    return f"""# Production tips — Phase {p["num"]}: {p["title"]}

## Cost

{t["cost"]}

## Latency

{t["latency"]}

## Reliability

{t["reliability"]}

## Observability

{t["observability"]}

## Scaling

{t["scaling"]}

## The boring checklist

{_join(t["checklist"])}

Production is not a later phase. It is a way of writing Tuesday's code.
"""


def challenge(p: dict[str, Any]) -> str:
    c = p["challenge"]
    return f"""# Challenge — Phase {p["num"]}: {p["title"]}

This is optional. It is also how you get interesting interview stories.

## {c["title"]}

{c["body"]}

**Constraints**

{_join(c["constraints"])}

**Success looks like**

{c["success"]}
"""


def solutions(p: dict[str, Any]) -> str:
    items = "\n\n".join(
        f"### {s['id']}\n\n{s['hint']}\n\n<details><summary>Approach (still not full code)</summary>\n\n{s['approach']}\n\n</details>"
        for s in p["solutions"]
    )
    return f"""# Solutions — Phase {p["num"]}: {p["title"]}

Spoilers. Try for 25 minutes first.

We give **hints and approaches**, not copy-paste repos. If you paste a full solution into your portfolio without understanding it, the interview will hurt.

{items}

Full working patterns related to this phase also live in [`code/`](./code/) and [EXAMPLES](../../EXAMPLES/).
"""


RENDERERS = {
    "README.md": readme,
    "Theory.md": theory,
    "Examples.md": examples,
    "Practice.md": practice,
    "Exercises.md": exercises,
    "Assignments.md": assignments,
    "Quiz.md": quiz,
    "Flashcards.md": flashcards,
    "Interview.md": interview,
    "Cheatsheet.md": cheatsheet,
    "MiniProject.md": miniproject,
    "Resources.md": resources,
    "FAQ.md": faq,
    "Debugging.md": debugging,
    "CommonMistakes.md": common_mistakes,
    "ProductionTips.md": production_tips,
    "Challenge.md": challenge,
    "Solutions.md": solutions,
}


def write_phase(root: Path, slug: str, payload: dict[str, Any]) -> None:
    dest = root / "phases" / slug
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "code").mkdir(exist_ok=True)
    (dest / "assets").mkdir(exist_ok=True)
    for name, fn in RENDERERS.items():
        (dest / name).write_text(fn(payload), encoding="utf-8")
    # starter code files
    for fname, content in payload.get("code_files", {}).items():
        path = dest / "code" / fname
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    readme_code = dest / "code" / "README.md"
    if not readme_code.exists():
        readme_code.write_text(
            f"# Code for Phase {payload['num']} — {payload['title']}\n\n"
            "Run from the phase folder or this directory. See Examples.md for the walkthrough.\n",
            encoding="utf-8",
        )
