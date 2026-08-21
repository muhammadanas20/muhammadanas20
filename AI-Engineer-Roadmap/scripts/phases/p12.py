from make_phase import C, E, EX, I, Q, asg, drill, mp, phase, th

PHASE = phase(
    num="12",
    title="Production AI / LLMOps",
    tagline="If you cannot trace it, cache it, evaluate it, or fall back, you do not operate it.",
    hours="10-14 days",
    difficulty="Hard",
    exit_ticket="Traces on every request, an eval gate in CI, cache, rate limit, and a fallback model.",
    objectives=[
        "Add tracing (OpenTelemetry / Langfuse / LangSmith).",
        "Run offline evals (Ragas, DeepEval, Promptfoo) in CI.",
        "Cache embeddings and safe answers.",
        "Rate limit and budget tokens.",
        "Route and fall back across models.",
    ],
    prerequisites=["A deployed or local RAG/chat app. Phase 8 evals started."],
    topics=["Monitoring", "tracing", "Langfuse", "LangSmith", "Promptfoo", "DeepEval", "Ragas", "caching", "rate limits", "fallback", "routing"],
    nav="[Home](../../README.md) · Prev: [Phase 11](../11-deployment/) · Next: [Phase 13 · Security](../13-security/)",
    theory=th(
        intro="""**LLMOps** is operations for systems that include models.

Classic ops: CPU, RAM, error rate.

LLMOps adds: tokens, cost, faithfulness, latency to first token, tool error rate, cache hit rate, eval score over time.

If you only watch HTTP 500s, your bot can be confidently wrong at 200 OK all week.""",
        one_liner="Operate quality, cost, and latency — not just uptime.",
        why="""Models drift (provider updates). Prompts change. Indexes rot. Costs spike on one viral tweet.

Without traces you cannot debug. Without evals you cannot ship. Without budgets you cannot sleep.""",
        if_missing="you would 'monitor' with print() and a credit card alert from OpenAI.",
        analogy="""An airplane cockpit.

- **Traces** = flight recorder (every request's retrieve → generate)
- **Metrics** = altimeter (p95, cost/1k, cache hit)
- **Evals** = inspection checklist before takeoff (CI) and in flight (sampled)
- **Cache** = using the same weather report for 30 seconds
- **Rate limit / budget** = fuel cap
- **Fallback** = second engine
- **Routing** = small plane for short hops, jet for cargo""",
        visual="""```mermaid
flowchart LR
  Req --> Cache
  Cache -->|hit| Out
  Cache -->|miss| Route
  Route --> Primary
  Primary -->|fail/timeout| Fallback
  Primary --> Trace
  Fallback --> Trace
  Trace --> Langfuse
  CI --> Evals
```""",
        architecture="""```mermaid
flowchart TB
  API --> OTel[OpenTelemetry]
  API --> Langfuse
  CI --> Promptfoo
  CI --> Ragas
  API --> RedisCache
  API --> RedisRL
  API --> Router
  Router --> Cheap
  Router --> Strong
```""",
        beginner="""**Trace:** a tree of spans: `http.request` → `retrieve` → `rerank` → `generate`. Each span has timing and attributes (model, token counts, chunk ids).

**Langfuse / LangSmith:** products that store these traces and let you click them. OpenTelemetry is the open standard some of them speak.

**Offline eval:** a JSONL of cases run in CI. Fail the build if faithfulness < threshold.

**Online eval:** sample 1% of prod traffic for a judge or human.

**Cache:**
- Embedding cache (hash of text)
- Exact prompt cache
- Semantic cache (embed the query, reuse answer if very close) — dangerous if freshness/PII matter

**Rate limit:** per user and per tenant. Token budgets better than request counts.

**Fallback:** if primary 429/5xx/timeout, call a second model or return a degraded answer.

**Routing:** classify intent → cheap vs strong model.""",
        intermediate="""**Promptfoo:** YAML of prompts/tests, compare models. Great for regression.

**DeepEval / Ragas:** RAG-focused metrics. Know their failure modes (LLM-as-judge bias).

**Semantic cache keys** must include tenant, prompt version, doc version.

**Idempotency** of evals: pin model versions. Providers silently update aliases (`gpt-4o` drifts). Pin dates when you can.

**SLOs:** e.g. TTFT p95 < 1.5s, eval faithfulness > 0.8, cost < $X/day.

**Error budgets** for quality, not only downtime.""",
        advanced="""**Shadow traffic:** new prompt version gets 10% of queries, answers not shown, scores compared.

**Bandits** for routing — overkill until you have volume.

**OpenTelemetry semantic conventions** for gen AI (evolving).

**PII in traces:** redaction. Never store raw prompts in a third party without a DPA if you are a company.

**Eval datasets as code.** Version them. Don't edit gold labels to make graphs pretty.""",
        production="""A weekly quality review beats a perfect dashboard nobody opens.

Alert on: cost spike, parse-fail rate, fallback rate, eval drop, p95.

When eval drops, check: index freshness, provider model change, prompt diff, retrieval recall.""",
        when="Any AI feature used by real humans or costing real money.",
        when_not="A weekend toy with 12 requests total. Don't build a platform before a product. Do still log tokens.",
        code_preview='''# fallback sketch
try:
    return await primary.complete(..., timeout=20)
except (TimeoutError, ProviderDown):
    return await backup.complete(...)
''',
        code_notes="Fallback is boring `try/except` plus metrics. Not a new religion.",
        ex_b="Log tokens and latency to CSV on each call.",
        ex_m="Wrap retrieve+generate in spans (even print-based). Add Redis exact cache.",
        ex_h="CI eval job that fails under threshold. Fallback test with a fake primary that times out.",
        project="Eval harness template — TEMPLATES/eval-harness.",
        interview_preview="What do you trace? How eval in CI? Semantic cache risks? How fallback?",
        flash_sample="**Q:** 200 OK means the answer was right?\n**A:** No.",
        mistakes_preview="Tracing PII to a SaaS without thought. Semantic cache across tenants. Alerting only on 500s. Unpinned model aliases in evals.",
        debug_preview="Cost doubled overnight (loop + no cache). Eval dropped (index empty after migrate).",
        best="Pin versions. Trace the path. Eval in CI. Budget. Fallback. Redact.",
        industry="Langfuse, LangSmith, Braintrust, Phoenix, Promptfoo, OpenTelemetry. Pick one tracer and one eval tool. Depth > a zoo.",
        perf="Cache embeddings first (safe). Then exact answers. Semantic last. Router saves money.",
        security="Redact traces. Tenant in cache keys. Don't cache personalized or permissioned answers globally.",
        refs="- Langfuse docs\n- Promptfoo\n- Ragas\n- DeepEval\n- OpenTelemetry",
        further="Hamel Husain evals. Eugene Yan. OpenAI evals cookbook.",
    ),
    examples=[
        EX(
            title="Exact cache + token budget",
            why="Two ops primitives in 40 lines.",
            code='''"""code/cache_budget.py"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

@dataclass
class Budget:
    used: int = 0
    limit: int = 100_000

    def charge(self, tokens: int) -> None:
        if self.used + tokens > self.limit:
            raise RuntimeError("budget")
        self.used += tokens

cache: dict[str, str] = {}

def key(prompt: str, model: str) -> str:
    return hashlib.sha256(f"{model}:{prompt}".encode()).hexdigest()

def complete(prompt: str, model: str, budget: Budget, call) -> str:
    k = key(prompt, model)
    if k in cache:
        return cache[k]
    text, tokens = call(prompt)
    budget.charge(tokens)
    cache[k] = text
    return text
''',
            line_by_line="Key includes model. Budget fail-closed. Cache skips charge on hit (you already paid once).",
            output="Second identical call is free and instant.",
            dry_run="miss → call → charge → store. hit → return.",
            memory="O(unique prompts) — use Redis + TTL in prod.",
            time="O(1) dict",
            space="O(n)",
            alternatives="Redis SET EX. Provider-side prompt caching.",
            optimization="TTL. Don't cache user-specific data without tenant in key.",
        ),
        EX(
            title="Router",
            why="Not every question needs the strongest model.",
            code='''"""code/router.py"""
from __future__ import annotations

def route(question: str) -> str:
    q = question.lower()
    if len(q) < 40 or q.startswith(("hi", "hello", "thanks")):
        return "cheap"
    if any(w in q for w in ("legal", "medical", "refund policy")):
        return "strong"
    return "cheap"

if __name__ == "__main__":
    print(route("hi"), route("What is the refund policy for EU customers?"))
''',
            line_by_line="A toy classifier. Production: a small model or rules + RAG type. Always log the decision.",
            output="cheap strong",
            dry_run="Length and keywords pick a bucket.",
            memory="O(1)",
            time="O(len(q))",
            space="O(1)",
            alternatives="Embedding similarity to examples; dedicated classifier.",
            optimization="Don't call a huge router model that costs more than the savings.",
        ),
    ],
    practice=[
        drill("Token spreadsheet", "A day of fake traffic. Cost it.", "You have a number."),
        drill("One tracer", "Langfuse local or cloud free, or just structured logs. Send 10 spans.", "You can click a request."),
        drill("Eval in pytest", "3 cases, assert output contains a phrase.", "CI-shaped."),
    ],
    exercises={
        "beginner": [
            E("CSV logger", "model, tokens, ms, cache_hit.", "50 rows from a script."),
            E("Budget", "Fail 429-like after N tokens.", "Test."),
        ],
        "medium": [
            E("Redis cache", "TTL 60s, tenant in key.", "Prove cross-tenant miss."),
            E("Fallback", "Primary raises, secondary returns, metric fallback=1.", "Test with monkeypatch."),
        ],
        "hard": [
            E("CI eval gate", "Ragas or custom score; fail < 0.7 on 10 cases.", "YAML in Actions."),
            E("Shadow prompt", "v2 runs in background, scores logged, v1 still served.", "No user-facing change."),
        ],
    },
    assignments=[
        asg(
            "ops-layer",
            "3–5 days",
            "Add to your RAG app: traces, Redis cache, rate limit, fallback, eval job. Write SLO.md.",
            ["code", "SLO.md", "screenshot of a trace or log"],
            ["tenant-safe cache", "CI eval", "cost field logged"],
        )
    ],
    quiz=[
        Q("200 OK implies", "Correct answer", "HTTP succeeded, not truth", "Faithfulness 1.0", "Cheap", "B", "Quality ≠ status."),
        Q("A trace is", "A stack of spans for one request", "A Docker image", "A JWT", "A vector", "A", "Recorder."),
        Q("Semantic cache danger", "It's slow", "Stale or cross-tenant answers", "It uses Redis", "It needs Docker", "B", "Correctness."),
        Q("Pin model versions because", "Aliases can drift", "It is prettier", "CI forbids dates", "Cosine", "A", "Drift."),
        Q("Fallback is for", "Happy path only", "Timeouts/429/5xx/parse fail", "CSS", "Embeddings dim", "B", "Degrade."),
        Q("LLM-as-judge risk", "Bias and cost", "It never works", "Illegal always", "Needs k8s", "A", "Use carefully."),
        Q("Rate limit unit for LLMs", "Preferably tokens/tenant", "Only CPU", "Only IP always", "GPU clocks", "A", "Tokens."),
        Q("Promptfoo is", "A GPU", "An eval/regression tool", "A vector DB", "Nginx", "B", "Evals."),
        Q("Cache key must include", "Tenant + prompt/model/doc version as needed", "Only the question text ever", "The user's password", "Nothing", "A", "Isolation."),
        Q("Eval in CI should", "Fail the build on large regressions", "Only run on your laptop", "Edit gold labels until green", "Use production PII", "A", "Gate."),
    ],
    flashcards=[
        C("LLMOps extra metrics?", "Tokens, cost, faithfulness, TTFT, cache hit, fallback rate."),
        C("Span?", "A timed unit of work inside a trace."),
        C("Offline vs online eval?", "Frozen set in CI vs sampled prod."),
        C("Why pin models?", "Aliases change under you."),
        C("Semantic cache?", "Reuse answers for similar queries — risky."),
        C("Router?", "Pick cheap vs strong path."),
        C("Shadow traffic?", "New version scores silently."),
        C("Langfuse?", "Trace/eval product."),
        C("Budget?", "Hard cap on tokens/money."),
        C("Redact traces?", "PII/secrets out of SaaS logs."),
    ],
    interview=[
        I("What do you monitor for an LLM app?", "Latency, errors, tokens, cost, cache, fallback, eval scores, retrieval empty rate — not only 500s.", "CPU only.", "SLOs and quality error budgets."),
        I("How do you eval in CI?", "Frozen JSONL, pinned model, threshold, fail build. Separate holdout.", "We eyeball on Friday.", "Flakes, cost of CI, sampling."),
        I("Design caching.", "Embedding cache always. Exact answer cache with TTL + versions + tenant. Semantic cache only if safe.", "Cache everything globally forever.", "Invalidation on ingest."),
        I("Provider is down.", "Timeouts, retries with jitter, fallback model, degrade to retrieval-only snippets, status page.", "Wait.", "Multi-vendor, queues."),
        I("Cost exploded.", "Traces: loops, k too big, no cache, retries on 400s, agent hops. Add budgets.", "Buy more credits first.", "Unit economics per feature."),
    ],
    whiteboard=[
        "SLO dashboard boxes for a RAG API.",
        "Cache key design for multi-tenant docs.",
        "CI eval pipeline.",
    ],
    interview_listen="quality+cost+latency as first-class, traces, pinned evals",
    cheatsheet={
        "remember": "Trace. Eval in CI. Pin models. Tenant in cache keys. Fallback. Budget.",
        "bash": "pytest tests/eval -q\n# langfuse / promptfoo CLIs as you choose",
        "python": "try: primary()\nexcept TimeoutError: fallback()",
        "decisions": "Exact cache first. Semantic cache later. Router if cost hurts.",
        "numbers": "Sample 1% online. TTFT SLO ~1–2s chat. Set a real $ daily cap.",
        "do_not": "PII traces. Cross-tenant cache. Unpinned aliases. 500-only alerts.",
    },
    miniproject=mp(
        name="ops-layer",
        time="2–4 days",
        difficulty="Hard",
        why="This is what separates wrappers from engineers.",
        story="I can show a trace, an eval number, and a cost cap.",
        must=["traces or structured spans", "CI eval", "cache", "fallback", "SLO.md"],
        should=["Langfuse or similar"],
        wont=["Build your own LangSmith clone"],
        architecture="```mermaid\nflowchart LR\nReq --> Cache --> Router --> Model --> Trace\n```",
        layout="../../TEMPLATES/eval-harness/",
        rubric=["screenshot/log", "threshold in CI", "tenant-safe cache"],
        stretch="Shadow prompt v2.",
    ),
    resources={
        "official": ["Langfuse", "LangSmith", "Promptfoo", "Ragas", "DeepEval", "OpenTelemetry"],
        "extra": ["Hamel on evals", "Braintrust docs"],
        "papers": ["Who Validates the Validators? (LLM-as-judge caveats)"],
    },
    faq=[
        {"q": "Langfuse or LangSmith?", "a": "Either. Open source / self-host bias → Langfuse. Already in LangChain ecosystem → LangSmith. Learn traces, not logos."},
        {"q": "Must I OpenTelemetry?", "a": "It's the portable layer. Fine to start with a vendor SDK."},
        {"q": "Eval cost?", "a": "Run small in CI (10–30 cases). Nightly full set. Don't judge 10k traces with GPT-4 every commit."},
    ],
    debugging=[
        {
            "title": "Eval score jumped 20%",
            "symptom": "Looks like a win.",
            "wrong": "Gold labels edited; judge model changed; leak.",
            "see": "Diff the dataset and judge version.",
            "fix": "Pin everything. Holdout.",
            "prevent": "Dataset version in the report.",
        },
        {
            "title": "Cache served another tenant's answer",
            "symptom": "Data leak.",
            "wrong": "Key = query only.",
            "see": "Redis keys.",
            "fix": "tenant_id in key. Flush.",
            "prevent": "Test two tenants same query.",
        },
    ],
    mistakes=[
        {"title": "Dashboard theater", "body": "20 graphs, no action.", "instead": "3 SLOs with alerts."},
        {"title": "Semantic cache on policy docs without version", "body": "Yesterday's policy.", "instead": "doc_version in key or skip cache."},
        {"title": "Retrying 400s", "body": "Paying for a bad prompt forever.", "instead": "Retry 429/5xx only."},
    ],
    prod_tips={
        "cost": "Budgets, routers, caches, smaller models, smaller k. Weekly cost review.",
        "latency": "TTFT SLO. Cache. Parallel retrieve. Don't chain 5 reflections on the hot path.",
        "reliability": "Fallback. Timeouts. Queue when overloaded.",
        "observability": "If you cannot click one user request end-to-end, you are not done.",
        "scaling": "Stateless API + Redis + PG. Tracer backend sized for span volume.",
        "checklist": ["spans", "eval gate", "budget", "fallback", "redaction", "tenant cache keys"],
    },
    challenge={
        "title": "Cut cost 30% without dropping holdout faithfulness more than 2 points",
        "body": "Router, cache, or smaller model. Ablation table.",
        "constraints": ["Holdout frozen"],
        "success": "A table a CFO and an engineer both accept.",
    },
    solutions=[
        {"id": "M2 fallback", "hint": "monkeypatch primary to sleep/raise.", "approach": "Assert secondary called once."},
        {"id": "H1 CI", "hint": "pytest -q tests/eval; exit 1 on threshold.", "approach": "Store scores as artifact."},
    ],
    code_files={
        "cache_budget.py": '''"""Exact cache + token budget."""
from __future__ import annotations

import hashlib
from dataclasses import dataclass


@dataclass
class Budget:
    used: int = 0
    limit: int = 100_000

    def charge(self, tokens: int) -> None:
        if self.used + tokens > self.limit:
            raise RuntimeError("budget")
        self.used += tokens


def key(prompt: str, model: str) -> str:
    return hashlib.sha256(f"{model}:{prompt}".encode()).hexdigest()
''',
        "router.py": '''"""Toy model router."""


def route(question: str) -> str:
    q = question.lower()
    if len(q) < 40 or q.startswith(("hi", "hello", "thanks")):
        return "cheap"
    if any(w in q for w in ("legal", "medical", "refund policy")):
        return "strong"
    return "cheap"


if __name__ == "__main__":
    print(route("hi"), route("What is the refund policy for EU customers?"))
''',
    },
)
