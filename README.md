# LangChain course projects

Personal practice repo for LangChain projects.

## Branches

| Branch | Project |
|--------|---------|
| `project/hello-world` | Animal poem app (Ollama) |
| `project/ai-job-search-agent` | AI Job Search agent |

## Setup (`project/hello-world`)

```bash
uv sync
cp .env.example .env   # add your keys
uv run python src/langchain_course/__init__.py
```

Requires [Ollama](https://ollama.com) with a local model (e.g. `gemma3:270m`, `llama3.2:1b`).
