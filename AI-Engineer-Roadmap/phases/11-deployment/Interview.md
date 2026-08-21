# Interview — Phase 11: Deployment

Answer out loud. Then read. Then answer again with the file closed.

If you only read these, you will freeze in the real room.

---

### Q1. Walk through your deploy.

**Expected answer (junior)**

Push → Actions test → build image SHA → registry → PaaS pulls → health → live. Rollback = previous SHA.

**Common mistakes**

I click upload on a website.

**Senior-level discussion**

Canary, migrations, secrets.
### Q2. How do you handle secrets?

**Expected answer (junior)**

Platform store, injected as env, .env.example committed, rotation plan.

**Common mistakes**

In the repo but it's private.

**Senior-level discussion**

SOPS, vault, OIDC.
### Q3. App 502s after deploy.

**Expected answer (junior)**

Logs, health, bind address, secret missing, migrations, OOM, proxy timeout vs model.

**Common mistakes**

Rebuild laptop.

**Senior-level discussion**

Systematic.
### Q4. Why not Kubernetes first?

**Expected answer (junior)**

Need the container story first. K8s is an orchestrator for many nodes. PaaS is enough for this app.

**Common mistakes**

K8s is always required to be senior.

**Senior-level discussion**

When k8s wins: many services, complex scheduling.
### Q5. CI vs CD?

**Expected answer (junior)**

CI = verify each change. CD = automatically/continuously ship those verified artifacts.

**Common mistakes**

They are the same letters so the same.

**Senior-level discussion**

Gates, environments, approvals.


---

## Whiteboard prompts

- Pipeline from git to HTTPS.
- Where buffering can kill SSE.
- Expand/contract migration around a deploy.

Spend 10 minutes each. Use the 8-box spine from [SYSTEM_DESIGN_GUIDE.md](../../SYSTEM_DESIGN_GUIDE.md) when the question is a system.

## Meta

Interviewers in this topic are listening for tagged artifacts, secrets, health, rollback — not a 40-box k8s diagram.
