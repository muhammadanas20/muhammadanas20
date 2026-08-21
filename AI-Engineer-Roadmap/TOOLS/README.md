# Tools map

Use few tools well. This is a map, not a shopping list.

## Local first

| Tool | Role |
| --- | --- |
| Python 3.11/3.12 | Language |
| uv / venv | Installer |
| VS Code | Editor |
| Git + GitHub | History |
| Docker Compose | Services |
| Postgres | Source of truth |
| Redis | Limits, cache |
| Ollama | Local LLMs |
| Chroma / pgvector | Vectors while learning |

## Production-shaped

| Tool | Role |
| --- | --- |
| FastAPI | HTTP |
| Qdrant | Vector DB |
| LangGraph | Graphs when you need them |
| MCP | Standard tool plug |
| Langfuse | Traces |
| Ragas / DeepEval / Promptfoo | Evals |
| GitHub Actions | CI |
| Fly / Render / Railway | First URL |

## Hosted models

OpenAI, Anthropic, Google, Groq — interchangeable behind your interface. Pin versions.

## Deliberately later

Kubernetes operators, fine-tuning platforms, GPU clusters, every agent framework at once.
