# Security cheatsheet

- Direct injection = user box
- Indirect = retrieved docs / tools / web
- Untrusted text is **data**
- No shell tools in prod
- RBAC in code
- Tenant tests that fail when filter omitted
- No secrets in git, images, prompts, traces
- Guardrails help; blast radius is the design
- Assume system prompt will leak
- OWASP LLM Top 10 — map it to your app
