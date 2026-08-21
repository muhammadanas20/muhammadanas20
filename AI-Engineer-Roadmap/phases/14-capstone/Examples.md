# Examples — Phase 14: Capstone

Type these. Do not paste and smile.

Every example includes: comments, line explanation, output, dry run, memory, complexity, alternatives, optimization.

Runnable copies live in [`code/`](./code/).



---

### Example 1. Scope card

Tape this to the monitor.

```python
"""code/scope.py — not runtime code: a checklist you print"""
MUST = [
    "one user story",
    "compose up",
    "auth",
    "eval number",
    "deployed URL",
    "threat model",
    "5-min demo script",
]
WONT = [
    "mobile app",
    "training a model",
    "kubernetes",
    "five agent personas",
]
print("MUST", len(MUST), "WONT", len(WONT))

```

**What every interesting line is doing**

If a new idea is not on MUST, it is WONT until after demo.

**Expected output**

```text
MUST 7 WONT 4
```

**Dry run**

Read lists. Feel the freeze.

**Memory**

n/a

**Time complexity:** n/a  
**Space complexity:** n/a

**Alternatives**

A Google doc. A whiteboard photo.

**Optimization**

Shorter MUST wins.

---

### Example 2. Demo timer outline

Rehearse with a clock.

```python
"""code/demo_script.txt shown here as a string"""
SCRIPT = """
0:00 Problem in one sentence
0:30 Architecture diagram
1:00 Happy path live
2:30 Citation / tool trace
3:30 Failure path (I don't know or denied tool)
4:00 Eval number + cost
4:30 What I'd do next
5:00 Stop
"""
print(SCRIPT)

```

**What every interesting line is doing**

Failure path builds more trust than a second happy path.

**Expected output**

```text
The script.
```

**Dry run**

Say it out loud with a timer.

**Memory**

n/a

**Time complexity:** 300s  
**Space complexity:** n/a

**Alternatives**

A Loom video backup.

**Optimization**

Cut until it fits 5:00.


---

When you finish, change one constant in each example and write the new output in `NOTES/`. If you cannot predict it, you did not learn it.
