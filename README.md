# blent-ai-customer-service-assistant

LangChain-based chatbot that answers e-commerce order questions in natural language by querying a SQL database in real time.

## Overview

LLM-based assistant that answers customer questions about their orders (status, delivery, payment) by querying a SQL database in real time. Includes semantic routing and prompt injection protection.

## Stack

- **Python** — via [uv](https://docs.astral.sh/uv/)
- **LangChain** — LLM orchestration
- **SQLite** — order database

## Requirements

[uv](https://docs.astral.sh/uv/) is required to manage dependencies and run the project.

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Getting started

```bash
uv sync
uv run python src/main.py
```
