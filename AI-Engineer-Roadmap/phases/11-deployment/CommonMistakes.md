# Common mistakes — Phase 11: Deployment

### 1. Building on a laptop and copying the image ad hoc

Not reproducible.

**Do this instead:** CI builds Linux images.

### 2. One long-lived AWS access key in GitHub

Leak = account takeover.

**Do this instead:** OIDC.

### 3. No rollback plan

You debug live for 3 hours.

**Do this instead:** Keep last 5 images. One command back.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
