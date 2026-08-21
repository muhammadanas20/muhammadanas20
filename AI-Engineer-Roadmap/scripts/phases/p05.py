PHASE = {
    "num": "5",
    "title": "LLM fundamentals",
    "tagline": "Treat the model as a component: tokens, context, temperature, tools, structured output, streaming.",
    "hours": "10-14 days",
    "difficulty": "Medium",
    "exit_ticket": "A client that streams, validates JSON with Pydantic, and performs one tool call.",
    "objectives": [
        "Explain transformers at a picture level (no need to derive backprop).",
        "Count tokens and relate them to cost and context limits.",
        "Control temperature, top-p, and stop sequences with intent.",
        "Write prompts that are versioned, testable, and not folklore.",
        "Use tool/function calling and structured outputs.",
        "Stream tokens and cancel.",
    ],
    "prerequisites": ["Phases 0–4. You can ship a FastAPI service in Docker."],
    "topics": [
        "Transformers (intuition)",
        "Tokens and context windows",
        "Embeddings intro",
        "Temperature / sampling",
        "Prompt engineering",
        "Tool calling",
        "Structured outputs",
        "Streaming",
    ],
    "nav": "[Home](../../README.md) · Prev: [Phase 4](../04-docker/) · Next: [Phase 6 · Embeddings](../06-embeddings-search/)",
    "theory": {
        "intro": """A **Large Language Model** predicts the next token given previous tokens.

That one sentence explains:

- Why it can lie (it predicts plausible text, not truth)
- Why long inputs cost money (more tokens in)
- Why it forgets the middle of a huge dump (attention is uneven)
- Why temperature changes personality (sampling)

You do not need to train GPT. You need to **drive** one without crashing the car.

We will use hosted APIs (OpenAI, Anthropic, Groq) **or** local Ollama. The ideas are the same. The HTTP envelopes differ.""",
        "one_liner": "An LLM is a next-token engine with a finite context window and no built-in truth.",
        "why": """If you cannot explain tokens, you cannot estimate cost.

If you cannot explain temperature, you will debug 'flaky JSON' for days.

If you cannot do tool calling, you will paste SQL results into prompts by hand.

If you cannot do structured output, your API will crash on `json.loads`.

This phase is the difference between a wrapper script and an AI engineer.""",
        "if_missing": "you would treat ChatGPT as a magic box and fail every interview that asks 'what is a token?'",
        "analogy": """A very well-read intern with no internet and a small desk.

- **Context window** = the size of the desk. If you dump 40 binders, the intern skims badly (lost in the middle).
- **Token** = a word-piece they write. You pay per piece. 'ChatGPT' might be 2–3 pieces, not one.
- **Temperature 0** = they always pick the most obvious next word (good for JSON, classification).
- **Temperature high** = they get creative (good for brainstorming, bad for invoices).
- **System prompt** = the employee handbook on the wall.
- **Tool calling** = they can fill a form to use the company database instead of guessing.
- **Structured output** = they must fill the form, not write an essay.
- **Streaming** = they speak while thinking so you are not staring at a silent intern for 8 seconds.""",
        "visual": """```mermaid
flowchart LR
  P[Prompt tokens] --> M[Model]
  M --> S[Sample next token]
  S --> O[Output tokens]
  O --> S
  T[Tools] -.-> M
  Schema[JSON schema] -.-> O
```""",
        "architecture": """```mermaid
sequenceDiagram
  participant App
  participant API as Model API
  participant Tool
  App->>API: messages + tools + schema
  API-->>App: tool_call: get_order(id)
  App->>Tool: get_order
  Tool-->>App: json
  App->>API: tool result
  API-->>App: stream final answer
```""",
        "beginner": """**Transformer** (2017): a neural net that uses **attention** — each token can look at other tokens to decide what matters. Stack many layers. Train on oceans of text. The result is a model that continues text.

**Token:** a chunk of text the model uses. `tiktoken` or the provider's tokenizer counts them. Rule of thumb: English ≈ 4 characters/token. Code and other languages differ.

**Context window:** max tokens of input+output (sometimes input and output have separate caps). Exceed it and the API errors or silently truncates.

**Messages:** `system`, `user`, `assistant`, and later `tool`. Chat models are trained on this schema.

**Temperature:** 0 = greedy / near-deterministic. Higher = more random. **top-p** (nucleus) cuts the tail of the distribution. For extraction, use 0.

**Prompt engineering:** writing the instructions. Production prompts are files with versions, not vibes in a Slack thread.

**Hallucination:** fluent falsehood. The model is not retrieving your docs unless you set that up (Phase 8).

**Embeddings (preview):** vectors that represent meaning. Used for search. Different models than chat, usually.""",
        "intermediate": """**Lost in the middle:** models use the start and end of a long context better than the middle. Dumping a whole PDF is a skill issue.

**Stop sequences:** tell the model to halt at `\\n\\n` or `}`. Less important with chat APIs, still useful.

**Logprobs:** scores for tokens. Useful for classification confidence. Not always available.

**Few-shot:** show examples in the prompt. Helps format. Costs tokens. Prefer schemas when the API supports them.

**Tool calling:** you declare functions (name, JSON schema). The model may return a structured call instead of prose. You run the function and send back the result. The model never actually 'runs code' unless you do.

**Structured outputs / JSON mode / JSON schema:** the API constrains tokens to valid JSON. Still validate with pydantic. Constraints reduce but do not eliminate wrong *values*.

**Streaming:** tokens arrive as events. UX + cancellation. You cannot hash the full answer until the end.

**Context vs memory:** the window is not long-term memory. You persist chats in Postgres (Phase 2) and retrieve (Phase 8).""",
        "advanced": """**Sampling details:** temperature scales logits; top-p filters; top-k; seed for approximate reproducibility (not a legal guarantee).

**Tokenizer mismatch:** counting with the wrong tokenizer mis-estimates cost and truncation.

**Prompt injection (preview of Phase 13):** untrusted text in the context can override instructions. Treat retrieved docs as data, not as system voice.

**Speculative decoding, MoE, reasoning models:** product names change. The engineering contract stays: tokens in, tokens out, tools, bills.

**Fine-tuning vs RAG vs prompt:** 
- Prompt: style, format, light facts
- RAG: changing or private facts
- Fine-tune: style/format at scale, or a new skill that examples can teach
Do not fine-tune to 'teach the employee handbook' that updates weekly.

**Provider differences:** OpenAI tools, Anthropic tools, Ollama's subset. Wrap behind your own interface.""",
        "production": """Version prompts in git (`prompts/v3_classify.txt`). Log model name, params, token counts, latency. Cap `max_tokens`. Set timeouts. Fallback models (Phase 12). Eval sets (Phase 8/12). Never send secrets in prompts. Budget dashboards.

The happy path is one call. Production is: timeout, 429, malformed JSON, empty tool args, safety refusal, truncated output.""",
        "when": "Language tasks: generate, classify, extract, route, tool-orchestrate, summarize with care.",
        "when_not": "When you need guaranteed facts without retrieval. When a regex or a SQL query is enough. When the user needs a numeric optimizer. When you cannot afford variance.",
        "code_preview": '''from pydantic import BaseModel

class OrderStatus(BaseModel):
    order_id: str
    status: str
    eta_days: int | None
# Send json schema of OrderStatus to the API.
# Validate the response with OrderStatus.model_validate_json(...)
''',
        "code_notes": "The schema is both the prompt and the validator. Two layers.",
        "ex_b": "Count tokens of a string. Classify tickets at temperature 0.",
        "ex_m": "Structured extraction of a resume into pydantic. Retry on ValidationError once.",
        "ex_h": "Tool loop: model can call get_time or get_weather (mocked). Max 3 hops. Stream the final answer.",
        "project": "Ticket classifier CLI + one tool — MiniProject.md.",
        "interview_preview": "Token? Temperature 0 when? RAG vs fine-tune? How tools work? Why JSON still needs pydantic.",
        "flash_sample": "**Q:** Does the model remember last week?\n**A:** Only if you send it again (or retrieve it).",
        "mistakes_preview": "temperature 1.0 for JSON. No max_tokens. Stuffing 200-page PDFs. Trusting JSON mode without validation. Fine-tuning to store facts.",
        "debug_preview": "Empty content because the model only returned a tool call. Truncated JSON. Off-by-tokenizer cost.",
        "best": "temp 0 for extraction. Schemas. Versioned prompts. Token logs. Timeouts. Smallest model that meets eval.",
        "industry": "OpenAI, Anthropic, Google, plus OSS via Ollama/vLLM. JSON schema / tool calling is table stakes on job posts.",
        "perf": "Prompt caching where available. Shorter prompts. Cheaper models for routing. Stream. Don't embed with a chat model.",
        "security": "No secrets in prompts. Treat user text as hostile (injection). Allow-list tools. Cap loops.",
        "refs": "- Vaswani et al. 2017 Attention Is All You Need\n- OpenAI / Anthropic docs\n- [Ollama](https://docs.ollama.com/)\n- Liu et al. 2023 Lost in the Middle",
        "further": "Anthropic 'Building effective agents'; OpenAI cookbook; Chip Huyen's LLM blogs.",
    },
    "examples": [
        {
            "title": "Structured output with a local-shaped client",
            "why": "Provider SDKs change. The pattern does not: schema in, validate out.",
            "code": '''"""code/structured.py"""
from __future__ import annotations

import json
from pydantic import BaseModel, Field, ValidationError

class Ticket(BaseModel):
    category: str = Field(pattern=r"^(billing|tech|other)$")
    priority: int = Field(ge=1, le=3)
    summary: str

def fake_model(prompt: str) -> str:
    # Pretend this string came from an LLM JSON mode
    return json.dumps({"category": "tech", "priority": 2, "summary": prompt[:80]})

def classify(text: str) -> Ticket:
    raw = fake_model(text)
    try:
        return Ticket.model_validate_json(raw)
    except ValidationError as exc:
        raise RuntimeError(f"model broke contract: {exc}") from exc

if __name__ == "__main__":
    print(classify("My login button 500s since the deploy"))
''',
            "line_by_line": "Ticket is the contract. fake_model stands in for OpenAI/Ollama. ValidationError becomes a runtime error you can retry or route.",
            "output": "category='tech' priority=2 summary='My login button 500s since the deploy'",
            "dry_run": "text → fake JSON → pydantic → Ticket. If category were 'banana', RuntimeError.",
            "memory": "O(n) in the JSON string.",
            "time": "O(n) parse",
            "space": "O(n)",
            "alternatives": "Instructor library; OpenAI parse=; Anthropic structured; outlines/jsonformer for local models.",
            "optimization": "Constrained decoding on local models to reduce retries.",
        },
        {
            "title": "A tiny tool loop",
            "why": "Agents (Phase 9) are this loop with extra state.",
            "code": '''"""code/tools.py"""
from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any

Tool = Callable[..., str]

def get_order(order_id: str) -> str:
    return json.dumps({"id": order_id, "status": "shipped"})

TOOLS: dict[str, Tool] = {"get_order": get_order}

def run_tool(name: str, args: dict[str, Any]) -> str:
    if name not in TOOLS:
        return json.dumps({"error": "unknown tool"})
    return TOOLS[name](**args)

# A fake model turn: it 'decides' to call a tool then answer.
turns = [
    {"type": "tool", "name": "get_order", "args": {"order_id": "A1"}},
    {"type": "text", "content": "Order A1 is shipped."},
]
for turn in turns:
    if turn["type"] == "tool":
        print("tool", turn["name"], run_tool(turn["name"], turn["args"]))
    else:
        print("final", turn["content"])
''',
            "line_by_line": "Allow-list TOOLS. Never eval arbitrary names. The model proposes; your code dispatches.",
            "output": "tool get_order {\"id\": \"A1\", \"status\": \"shipped\"}\\nfinal Order A1 is shipped.",
            "dry_run": "Loop turns. First dispatches get_order. Second prints. No infinite loop because we used a list, not while True — production needs a max_steps.",
            "memory": "O(tools + conversation)",
            "time": "O(steps)",
            "space": "O(steps)",
            "alternatives": "OpenAI tool_calls array; LangGraph later; MCP later.",
            "optimization": "Parallel tool calls when independent. Timeouts per tool.",
        },
    ],
    "practice": [
        {"title": "Token gym", "body": "Install tiktoken or use Ollama's token count. Measure 3 strings: English, code, Urdu/emoji. Write the ratios.", "done": "You stopped believing 1 word = 1 token."},
        {"title": "Temperature", "body": "Same extraction prompt at 0 and 1.0, 10 times each. Count schema failures.", "done": "A small table."},
        {"title": "Ollama or hosted", "body": "Run one chat completion locally or on a free/cheap API. Log tokens and latency.", "done": "A line in NOTES/."},
    ],
    "exercises": {
        "beginner": [
            {"title": "Prompt file", "body": "Move a prompt to prompts/classify_v1.txt and load it in code. Change to v2 without editing Python logic.", "constraints": "Git diff shows the prompt, not a 200-line py."},
            {"title": "max_tokens", "body": "Summarize a paragraph with max_tokens=16. Observe truncation. Handle it.", "constraints": "Detect finish_reason."},
        ],
        "medium": [
            {"title": "Resume extractor", "body": "Pydantic Resume model. Parse a messy text resume.", "constraints": "Retry once with error message in the prompt."},
            {"title": "Cost estimator", "body": "Function that given model prices and token counts returns USD. Table for 1k requests.", "constraints": "Prices in a config file, not hardcoded in three places."},
        ],
        "hard": [
            {"title": "Real tool loop", "body": "Against Ollama or OpenAI: model may call `add(a,b)` or `now()`. Max 4 steps. Stream final.", "constraints": "Unknown tools return an error object, not an exception crash."},
        ],
    },
    "assignments": [
        {
            "title": "Ticket brain",
            "time": "6–10 hours",
            "brief": "CLI + optional FastAPI: classify support tickets into pydantic, optional tool `lookup_user(id)` mocked, stream explanation, log tokens to CSV.",
            "deliverables": ["code", "prompt file versioned", "20-ticket eval accuracy", "README"],
            "rubric": ["temp 0", "validation", "token log", "eval number", "no secrets"],
        }
    ],
    "quiz": [
        {"q": "An LLM fundamentally:", "choices": {"A": "Queries Google", "B": "Predicts next tokens", "C": "Stores your PDFs in weights by default", "D": "Guarantees truth"}, "answer": "B", "explain": "Next-token prediction."},
        {"q": "A token is:", "choices": {"A": "Always one English word", "B": "A model-specific text piece", "C": "A Docker layer", "D": "A JWT"}, "answer": "B", "explain": "Tokenizer dependent."},
        {"q": "Temperature 0 is best for:", "choices": {"A": "Poetry", "B": "JSON extraction", "C": "Diversity of jokes", "D": "Training"}, "answer": "B", "explain": "Low variance."},
        {"q": "Context window is:", "choices": {"A": "Infinite memory", "B": "A finite token budget for the prompt+response", "C": "RAM of the GPU only", "D": "Your Postgres size"}, "answer": "B", "explain": "Finite."},
        {"q": "Tool calling means:", "choices": {"A": "The model SSHs into prod", "B": "The model proposes a structured function call that YOUR code runs", "C": "Fine-tuning", "D": "Embeddings"}, "answer": "B", "explain": "You dispatch."},
        {"q": "JSON mode guarantees:", "choices": {"A": "Correct business values", "B": "Mostly valid JSON shape (still validate)", "C": "Citations", "D": "Low cost"}, "answer": "B", "explain": "Shape ≠ truth."},
        {"q": "Lost in the middle means:", "choices": {"A": "GPUs overheat", "B": "Models use mid-context worse than edges", "C": "Redis TTL", "D": "Docker layers"}, "answer": "B", "explain": "Liu et al."},
        {"q": "Fine-tune to store a weekly-changing policy?", "choices": {"A": "Yes always", "B": "No — use RAG / retrieval", "C": "Yes with temperature 2", "D": "Use Redis only"}, "answer": "B", "explain": "Facts that change → retrieve."},
        {"q": "Streaming helps:", "choices": {"A": "TTFT UX and cancellation", "B": "Accuracy always", "C": "Token prices", "D": "SQL"}, "answer": "A", "explain": "UX."},
        {"q": "System prompt is:", "choices": {"A": "A secret key", "B": "High-level instructions for the model", "C": "A vector DB", "D": "A healthcheck"}, "answer": "B", "explain": "Handbook."},
    ],
    "flashcards": [
        {"q": "What is a token?", "a": "A chunk of text the tokenizer emits; billing and limits use it."},
        {"q": "Why temp 0 for extraction?", "a": "Less sampling noise, more stable JSON."},
        {"q": "Does the model know your docs?", "a": "Not unless they were in training (stale/public) or you send/retrieve them."},
        {"q": "What is a tool call?", "a": "Structured request from the model for you to run a function."},
        {"q": "Why pydantic after JSON mode?", "a": "Wrong types/values, extra fields, provider bugs."},
        {"q": "Context vs memory?", "a": "Context is this request's desk; memory is your DB."},
        {"q": "Name three roles.", "a": "system, user, assistant (plus tool)."},
        {"q": "RAG vs fine-tune in one line?", "a": "RAG for facts; fine-tune for style/skill."},
        {"q": "What is TTFT?", "a": "Time to first token."},
        {"q": "Why cap max_tokens?", "a": "Cost and runaway generations."},
    ],
    "interview": [
        {
            "q": "What is a token and why do I care?",
            "junior": "A tokenizer piece. Billing, rate limits, and context windows are in tokens. English ~4 chars/token but measure.",
            "mistakes": "1 word = 1 token always. Confusing tokens with embeddings.",
            "senior": "Tokenizer mismatch, multilingual cost, prompt caching billed differently, output vs input prices.",
        },
        {
            "q": "When do you fine-tune vs RAG vs prompt?",
            "junior": "Prompt first. RAG for private/changing facts. Fine-tune for style or a skill with many examples.",
            "mistakes": "Fine-tune the employee handbook.",
            "senior": "Evals, cost of training, latency, on-policy data, LoRA, catastrophic forgetting, eval regressions.",
        },
        {
            "q": "How does function calling work end to end?",
            "junior": "Declare schema, model returns tool call, app executes, app sends result, model answers. Allow-list.",
            "mistakes": "The model executes SQL itself. eval() on tool name.",
            "senior": "Parallel calls, idempotency, human-in-the-loop, injection via tool results, max hops.",
        },
        {
            "q": "The model returned invalid JSON. Now what?",
            "junior": "Validate, retry with error, lower temperature, use JSON schema mode, eventually fail closed.",
            "mistakes": "regex salvage forever; ignore the error.",
            "senior": "Constrained decoding, repair models, metrics on parse-fail rate, fallback to a bigger model.",
        },
        {
            "q": "Why not put the entire corpus in the prompt?",
            "junior": "Token cost, latency, context limits, lost-in-the-middle, PII sprawl.",
            "mistakes": "128k context means we are done with RAG.",
            "senior": "Needle-in-haystack benches vs real docs, cache, security, and still needing citations.",
        },
    ],
    "whiteboard": [
        "Draw a tool-call loop with a max-step guard.",
        "Estimate monthly cost: 10k chats/day, 1.5k tokens in, 400 out, pick a price.",
        "Compare dumping a PDF vs RAG for a 200-page policy.",
    ],
    "interview_listen": "tokens, variance, tools-as-your-code, RAG vs weights",
    "cheatsheet": {
        "remember": "Next-token ≠ truth. Temp 0 extract. Validate JSON. You run tools. Context is finite.",
        "bash": "ollama run llama3.2\nuv pip install openai tiktoken pydantic",
        "python": "Ticket.model_validate_json(raw)  # never json.loads hope",
        "decisions": "Facts change → retrieve. Format → schema. Style at scale → fine-tune. Regex enough → no LLM.",
        "numbers": "~4 chars/token English. Context 8k–200k+ depending on model. Cap tool hops 3–8.",
        "do_not": "Secrets in prompts. Unbounded loops. temp 1 for invoices. Fine-tune weekly facts.",
    },
    "miniproject": {
        "name": "ticket-brain",
        "time": "1–2 days",
        "difficulty": "Medium",
        "why": "Structured output + tools is the heart of production LLM features.",
        "story": "I paste a support email; I get a Ticket object and an optional user lookup.",
        "must": ["pydantic Ticket", "prompt file", "token log", "one tool", "eval on ≥15 samples"],
        "should": ["FastAPI endpoint", "stream explanation"],
        "wont": ["Full RAG", "Fine-tune"],
        "architecture": "```mermaid\nflowchart LR\nEmail --> Prompt --> Model --> Validate --> Ticket\nModel --> Tool\n```",
        "layout": "prompts/classify_v1.txt src/ticket_brain/ tests/ fixtures/",
        "rubric": ["eval % reported", "parse-fail % reported", "README costs"],
        "stretch": "Compare two models on the same 15 tickets.",
    },
    "resources": {
        "official": [
            "[OpenAI docs](https://platform.openai.com/docs)",
            "[Anthropic docs](https://docs.anthropic.com/)",
            "[Ollama](https://docs.ollama.com/)",
        ],
        "extra": ["OpenAI cookbook", "Anthropic prompt engineering", "Simon Willison LLM CLI"],
        "papers": [
            "Attention Is All You Need (2017)",
            "Lost in the Middle (2023)",
            "ReAct (2022) — preview of agents",
        ],
    },
    "faq": [
        {"q": "I have no API budget.", "a": "Ollama + a small model. Groq free tiers sometimes exist. This phase works locally."},
        {"q": "Which model?", "a": "The cheapest that passes your eval. Record the name and date."},
        {"q": "Is ChatGPT Plus enough?", "a": "The web UI is not an API. You cannot version, log, or evaluate it like a component."},
    ],
    "debugging": [
        {
            "title": "content is None",
            "symptom": "You print message.content and it's empty.",
            "wrong": "Assuming every turn is text. It may be a tool_call.",
            "see": "Log the raw response object.",
            "fix": "Branch on tool vs text.",
            "prevent": "Typed response handling.",
        },
        {
            "title": "JSON cut in half",
            "symptom": "ValidationError unexpected end.",
            "wrong": "max_tokens too small or output too chatty before JSON.",
            "see": "finish_reason=length.",
            "fix": "Raise max_tokens, instruct 'JSON only', use schema mode.",
            "prevent": "Monitor finish_reason.",
        },
    ],
    "mistakes": [
        {"title": "Prompt in a Slack screenshot as the source of truth", "body": "Nobody can review or rollback.", "instead": "File in git with a version field logged on each call."},
        {"title": "temperature=1 for extraction", "body": "Random JSON, random categories.", "instead": "0 or 0.1."},
        {"title": "Letting the model invent tool results", "body": "It will. Fluently.", "instead": "If a tool fails, send the error; do not ask it to guess the order status."},
    ],
    "prod_tips": {
        "cost": "Log tokens. Alert on daily budget. Cache identical prompts. Smaller model for classification.",
        "latency": "Stream. Shrink prompts. Parallelize independent calls. TTFT SLO.",
        "reliability": "Timeouts, retries on 429/5xx, fallback model, fail closed on parse.",
        "observability": "model, prompt_version, tokens, latency, parse_ok. Phase 12 adds traces.",
        "scaling": "The bottleneck is usually the provider RPM. Queue. Don't hot-loop.",
        "checklist": ["temp set on purpose", "max_tokens", "validate", "timeout", "token log", "prompt version"],
    },
    "challenge": {
        "title": "Provider adapter",
        "body": "One interface `complete(messages, tools, schema)` with OpenAI and Ollama backends. Tests fake both.",
        "constraints": ["No if openai in business logic", "Feature flag env"],
        "success": "Switching providers is an env var.",
    },
    "solutions": [
        {"id": "M1 resume", "hint": "On ValidationError, second call includes exc.errors().", "approach": "Cap at 1 retry to avoid cost loops."},
        {"id": "H1 tools", "hint": "while steps < 4: if tool_calls: dispatch else: stream break.", "approach": "Allow-list names. json.loads args inside try."},
    ],
    "code_files": {
        "structured.py": '''"""Schema-validate a fake LLM JSON response."""
from __future__ import annotations

import json

from pydantic import BaseModel, Field, ValidationError


class Ticket(BaseModel):
    category: str = Field(pattern=r"^(billing|tech|other)$")
    priority: int = Field(ge=1, le=3)
    summary: str


def fake_model(prompt: str) -> str:
    return json.dumps({"category": "tech", "priority": 2, "summary": prompt[:80]})


def classify(text: str) -> Ticket:
    raw = fake_model(text)
    try:
        return Ticket.model_validate_json(raw)
    except ValidationError as exc:
        raise RuntimeError(f"model broke contract: {exc}") from exc


if __name__ == "__main__":
    print(classify("My login button 500s since the deploy"))
''',
        "tools.py": '''"""Allow-listed tool dispatch — the heart of agents."""
from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any

Tool = Callable[..., str]


def get_order(order_id: str) -> str:
    return json.dumps({"id": order_id, "status": "shipped"})


TOOLS: dict[str, Tool] = {"get_order": get_order}


def run_tool(name: str, args: dict[str, Any]) -> str:
    if name not in TOOLS:
        return json.dumps({"error": "unknown tool"})
    return TOOLS[name](**args)


def main() -> None:
    turns = [
        {"type": "tool", "name": "get_order", "args": {"order_id": "A1"}},
        {"type": "text", "content": "Order A1 is shipped."},
    ]
    for turn in turns:
        if turn["type"] == "tool":
            print("tool", turn["name"], run_tool(turn["name"], turn["args"]))
        else:
            print("final", turn["content"])


if __name__ == "__main__":
    main()
''',
    },
}
