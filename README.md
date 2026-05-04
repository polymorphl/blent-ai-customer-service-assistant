# blent-ai-customer-service-assistant

LangChain-based chatbot that answers e-commerce order questions in natural language by querying a SQL database in real time.

## Overview

LLM-based assistant that answers customer questions about their orders (status, delivery, payment) by querying a SQL database in real time. Includes semantic routing and prompt injection protection.

## Stack

- **Python** — via [uv](https://docs.astral.sh/uv/)
- **LangChain** — LLM orchestration
- **Mistral API** — LLM provider (free tier)
- **SQLite** — order database

## Requirements

[uv](https://docs.astral.sh/uv/) is required to manage dependencies and run the project.

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Configuration

This project requires a Mistral API key (free tier available).

1. Create an account at [console.mistral.ai](https://console.mistral.ai)
2. Go to **API Keys** and generate a new key
3. Copy `.env.example` to `.env` and fill in your key:

```bash
cp .env.example .env
```

```env
MISTRAL_API_KEY=your_api_key_here
```

## Getting started

```bash
uv sync
uv run python -m src.main
```

## Running tests

```bash
uv run pytest
```
