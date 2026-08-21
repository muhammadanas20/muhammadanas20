# Common mistakes — Phase 13: Security

### 1. Security as a system prompt paragraph

The attacker writes a longer paragraph.

**Do this instead:** Code-level privilege.

### 2. Logging Authorization headers

Tokens in the log store.

**Do this instead:** Redact middleware.

### 3. One shared vector namespace

Tenant B's PDFs in tenant A's answers.

**Do this instead:** Filter + tests + maybe separate collections.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
