# Resume guide for AI engineer roles

Your resume has 20 seconds. A recruiter is not impressed that you "are passionate about AI."

They are looking for **proof you shipped systems that use models as components.**

---

## The only structure you need

```
Name  ·  city  ·  email  ·  github  ·  linkedin  ·  live demo
One line: what you build (not who you are)

EXPERIENCE  (or PROJECTS if you have little experience)
  Company / Project — Role  dates
  • verb + system + constraint + result

PROJECTS
  • 3 max for juniors. Links. Stack. One metric each.

SKILLS
  grouped: Languages · Backend · AI/LLM · Data · Infra

EDUCATION
```

One page until you have 8+ years.

---

## Bad vs good bullets

**Bad**

> Worked on a chatbot using LangChain and OpenAI.

**Why it fails:** no system, no constraint, no result, vendor name as identity.

**Good**

> Built a FastAPI RAG service over 1.2k internal Markdown docs with hybrid search + rerank; cut unsupported answers from 31% to 9% on a 40-question eval set; p95 latency 1.8s.

**Why it works:** architecture words a staff engineer recognizes, a metric, a constraint.

---

## Formula

`Verb` + `what you built` + `how (1–2 techniques)` + `constraint` + `result`

Verbs that sound like engineering: built, designed, shipped, reduced, instrumented, containerized, evaluated, restricted, cached, deployed.

Verbs that sound like a course: learned, explored, played with, prompted.

---

## Project bullets you can steal (after you do the work)

Replace numbers with yours. Fake numbers are worse than no numbers.

**PDF Chat**

> Shipped a Dockerized PDF Q&A API (FastAPI, Postgres/pgvector, rerank). Added Ragas faithfulness checks in CI; blocked merges below 0.75. Deployed to Fly.io with request tracing.

**SQL Agent**

> Built a read-only SQL agent with tool allow-lists and a hard row limit. Logged every tool call. Zero `DROP`/`DELETE` in 200 adversarial prompts.

**Support assistant**

> Designed a retrieval pipeline with metadata filters per tenant. Cached frequent embeddings. Estimated $0.03 / 1k queries at the chosen model mix.

---

## Skills section (honest)

Do not list a vector database you cannot install.

```
Languages:  Python, SQL
Backend:    FastAPI, Pydantic, PostgreSQL, Redis
AI:         RAG, embeddings, tool calling, LangGraph, MCP, evals (Ragas)
Infra:      Docker, GitHub Actions, Fly.io
```

"LangChain" alone is not a skill. "Designed a RAG pipeline" is.

---

## ATS and keywords

Job posts will mention: Python, FastAPI, AWS, RAG, LangChain, Docker, PostgreSQL, LLM, vector database, LangGraph, evaluation.

Mirror **words you truly have**. Put them in skills and in bullets.

Do not title yourself "Senior LLM Architect" as a student. `AI Engineer (projects)` or `Software Engineer · LLM applications` is fine.

---

## GitHub is part of the resume

Hiring managers click.

Each pinned repo needs:

- A README with a diagram
- How to run in 10 lines
- A screenshot or GIF
- License
- Recent commits (not one dump from 11 months ago)

See [CHECKLIST.md](./CHECKLIST.md) for portfolio-ready.

---

## Common resume mistakes in this field

1. Listing 14 frameworks and 0 metrics
2. "Fine-tuned GPT" when you meant "wrote a prompt"
3. Screenshots of ChatGPT in a browser as a "project"
4. No link to code
5. Skills you cannot survive a 10-minute probe on
6. Passive voice everywhere
7. GPA as the first line (put it under education if at all)

---

## Before you send

- [ ] One page
- [ ] Every project has a URL
- [ ] Numbers are real
- [ ] PDF is selectable text (not a screenshot)
- [ ] Filename: `Firstname_Lastname_AI_Engineer.pdf`
- [ ] You can talk for 5 minutes about every bullet
