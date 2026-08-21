# Solutions — Phase 2: SQL, Postgres, and Redis

Spoilers. Try for 25 minutes first.

We give **hints and approaches**, not copy-paste repos. If you paste a full solution into your portfolio without understanding it, the interview will hurt.

### B1 join

JOIN users ON ... ORDER BY created_at DESC LIMIT 20

<details><summary>Approach (still not full code)</summary>

Index (conversation_id, created_at desc).

</details>

### M2 stampede

SET lock key NX EX 10 while computing.

<details><summary>Approach (still not full code)</summary>

Only one worker fills cache; others wait or serve stale.

</details>

Full working patterns related to this phase also live in [`code/`](./code/) and [EXAMPLES](../../EXAMPLES/).
