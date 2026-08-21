# Solutions — Phase 3: FastAPI

Spoilers. Try for 25 minutes first.

We give **hints and approaches**, not copy-paste repos. If you paste a full solution into your portfolio without understanding it, the interview will hurt.

### M1 JWT

python-jose, HTTPBearer, exp claim.

<details><summary>Approach (still not full code)</summary>

Login checks password hash (passlib) then encode.

</details>

### H1 disconnect

request.is_disconnected in the generator loop.

<details><summary>Approach (still not full code)</summary>

Break and cancel upstream.

</details>

Full working patterns related to this phase also live in [`code/`](./code/) and [EXAMPLES](../../EXAMPLES/).
