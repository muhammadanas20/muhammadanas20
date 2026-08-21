# Solutions — Phase 5: LLM fundamentals

Spoilers. Try for 25 minutes first.

We give **hints and approaches**, not copy-paste repos. If you paste a full solution into your portfolio without understanding it, the interview will hurt.

### M1 resume

On ValidationError, second call includes exc.errors().

<details><summary>Approach (still not full code)</summary>

Cap at 1 retry to avoid cost loops.

</details>

### H1 tools

while steps < 4: if tool_calls: dispatch else: stream break.

<details><summary>Approach (still not full code)</summary>

Allow-list names. json.loads args inside try.

</details>

Full working patterns related to this phase also live in [`code/`](./code/) and [EXAMPLES](../../EXAMPLES/).
