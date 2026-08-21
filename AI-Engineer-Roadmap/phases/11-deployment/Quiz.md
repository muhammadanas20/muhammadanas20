# Quiz — Phase 11: Deployment

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

1. latest tag in prod
    A) Best
    B) Not reproducible
    C) Required by Docker
    D) Encrypts
2. healthz vs readyz
    A) Same
    B) Live vs ready for traffic
    C) Only k8s has them
    D) JWT things
3. Secrets belong in
    A) Git
    B) Platform secret store
    C) Docker image layers
    D) README
4. SSE behind Nginx
    A) Always fine
    B) May buffer; disable proxy buffering
    C) Impossible
    D) Needs UDP
5. CI should run on
    A) Only your Mac
    B) Linux runners typically
    C) iOS
    D) Windows 95
6. Rollback means
    A) Rewrite history
    B) Put the previous good image back in service
    C) Delete GitHub
    D) Scale to 0 forever
7. Bind 127.0.0.1 in a container
    A) Reachable from the internet
    B) Only inside the container
    C) Required
    D) Faster TLS
8. PaaS vs hyperscaler
    A) PaaS is less mopping, less control
    B) PaaS is always cheaper at infinite scale
    C) AWS is simpler than Render for hello world
    D) They are identical
9. Kubernetes Pod is
    A) A physical server
    B) One or more containers scheduled together
    C) A JWT
    D) A prompt
10. OIDC from GitHub to cloud
    A) Long-lived keys in secrets
    B) Short-lived federation, better
    C) A vector index
    D) A reranker

---

<details>
<summary>Answers (spoiler)</summary>

1. **B** — Pin SHA.
2. **B** — Two signals.
3. **B** — Not git.
4. **B** — Buffering.
5. **B** — ubuntu-latest.
6. **B** — Previous image.
7. **B** — Use 0.0.0.0.
8. **A** — Tradeoff.
9. **B** — Sketch level.
10. **B** — Prefer OIDC.

</details>
