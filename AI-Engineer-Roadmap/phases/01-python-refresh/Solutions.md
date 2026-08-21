# Solutions — Phase 1: Python refresh

Spoilers. Try for 25 minutes first.

We give **hints and approaches**, not copy-paste repos. If you paste a full solution into your portfolio without understanding it, the interview will hurt.

### B1 windows

for i in range(0, n-size+1, size-overlap): yield xs[i:i+size]

<details><summary>Approach (still not full code)</summary>

Careful with overlap >= size (illegal). Validate.

</details>

### H1 cancel

asyncio.timeout or task.cancel(); yield inside try; finally set flag.

<details><summary>Approach (still not full code)</summary>

Don't catch BaseException unless you re-raise.

</details>

Full working patterns related to this phase also live in [`code/`](./code/) and [EXAMPLES](../../EXAMPLES/).
