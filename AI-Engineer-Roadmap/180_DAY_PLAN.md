# 180-day plan — job-ready depth

**Who:** working a job or school, 10–15 hours/week, or anyone who wants the whole course.

**Goal:** junior AI engineer offers. Not "I watched a RAG video."

This is the intended path. The 90-day plan is a compression of this.

---

## Month-by-month

| Month | Weeks | Phases | You should be able to say |
| ---: | ---: | --- | --- |
| 1 | 1–4 | 0, 1, start 2 | My environment is boring and my Python is typed |
| 2 | 5–8 | 2, 3, 4 | I ship APIs in Docker with Postgres and Redis |
| 3 | 9–12 | 5, 6 | I treat LLMs like components with schemas |
| 4 | 13–16 | 7, 8 | I can defend a RAG design and show evals |
| 5 | 17–22 | 9, 10, start 11 | I can build an agent and an MCP server |
| 6 | 23–26 | 11, 12, 13, 14 | I operate, secure, and present a product |

Week-level table: [WEEKLY_PLAN.md](./WEEKLY_PLAN.md)

---

## Milestones (put these on a calendar)

| Day | Milestone | Evidence |
| ---: | --- | --- |
| 14 | Lab repo exists | Public GitHub, Actions badge optional |
| 45 | API stack | Compose file, JWT, streaming stub |
| 70 | First LLM feature | Structured output + tool |
| 100 | RAG v1 | PDF chat, 25-question eval |
| 130 | Agent v1 | SQL or research agent with traces |
| 150 | Production | Public URL, CI eval gate |
| 180 | Capstone freeze | Design doc + demo script + resume |

If you miss a milestone by more than 10 days, cut scope. Do not silently extend forever.

---

## Depth add-ons (only on this plan)

These are skipped in the 90-day sprint. Do them here.

- Week 14: Qdrant **and** pgvector, not just Chroma
- Week 16: one advanced RAG pattern fully implemented (Corrective or Self-RAG)
- Week 18: GraphRAG toy on a small corpus (so you know when it is overkill)
- Week 21: CrewAI or PydanticAI after LangGraph, as a comparison write-up
- Week 24: second cloud or a tiny Kubernetes kind cluster
- Week 26: load test the API (even `hey` or `k6` for 2 minutes)

---

## Interview cadence

Start **day 90**, not day 170.

| Window | Practice |
| --- | --- |
| Days 90–120 | 3 RAG / LLM fundamentals questions per day |
| Days 120–150 | System design twice a week ([SYSTEM_DESIGN/](./SYSTEM_DESIGN/)) |
| Days 150–180 | Full mocks: 45-min coding + 30-min design + 15-min project deep dive |

Use [INTERVIEW_PREP.md](./INTERVIEW_PREP.md).

---

## Application cadence

| Window | Volume |
| --- | --- |
| Days 120–150 | Resume v2, 5 conversations (alumni, Discord, LinkedIn) |
| Days 150–180 | 8–12 *tailored* applications per week |

Spray-and-pray 200 times is not a strategy. See [JOB_SEARCH_GUIDE.md](./JOB_SEARCH_GUIDE.md).

---

## Energy management

AI engineering learning dies in two ways:

1. Tutorial fog — many tools, no repo
2. Capstone infinity — rewriting the same chat UI

Countermeasures:

- One mini-project per phase, then **stop**
- Capstone feature freeze on day 165
- Days 166–180 are polish, evals, and talking practice

You are training for a job, not for a perfect architecture diagram.
