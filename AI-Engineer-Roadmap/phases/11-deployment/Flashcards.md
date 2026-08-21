# Flashcards — Phase 11: Deployment

Say the answer. Then open. Do the deck two days later. That is the whole spaced-repetition system.

**Q1.** 12-factor config?

<details><summary>Answer</summary>

Env vars, not baked files.

</details>

**Q2.** Where is TLS terminated often?

<details><summary>Answer</summary>

The PaaS / load balancer.

</details>

**Q3.** Why tag with git SHA?

<details><summary>Answer</summary>

Traceability and rollback.

</details>

**Q4.** Smoke test?

<details><summary>Answer</summary>

A tiny request after deploy proving liveness.

</details>

**Q5.** Scale to zero cost?

<details><summary>Answer</summary>

Cheap, cold start latency.

</details>

**Q6.** GHCR?

<details><summary>Answer</summary>

GitHub Container Registry.

</details>

**Q7.** readyz 503?

<details><summary>Answer</summary>

Stop sending traffic.

</details>

**Q8.** Migrations when?

<details><summary>Answer</summary>

Before new code needs the new schema (expand first).

</details>

**Q9.** Nginx role?

<details><summary>Answer</summary>

Reverse proxy, TLS, routing, static.

</details>

**Q10.** Minimum k8s vocab?

<details><summary>Answer</summary>

Pod, Deployment, Service, Ingress.

</details>
