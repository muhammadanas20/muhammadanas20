# Cheatsheet — Phase 13: Security

Print or pin. This is not a substitute for Theory.md.

## Remember

Untrusted data ≠ instructions. No dangerous tools. Tenant tests. No secrets in prompts/git/logs. Guardrails help, code enforces.

## Commands / snippets

```bash
gitleaks detect
pytest tests/security -q
```

```python
if not can(role, tool): raise PermissionError
```

## Decision tree

Side effect? HITL or don't ship. Multi-tenant? filter+test. PII traces? redact.

## Numbers

Keep a living file of 20+ injection cases in CI.

## Do not

shell. keys in prompts. trust retrieved text. skip tenant tests.
