# Challenge — Phase 3: FastAPI

This is optional. It is also how you get interesting interview stories.

## OAuth2 login

Add 'Login with GitHub' (or a fake OIDC) and issue your JWT after callback.

**Constraints**

- No secret in frontend
- State param against CSRF

**Success looks like**

A user can log in without you storing their GitHub password (you never should).
