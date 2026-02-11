# Smalls Bot (Safe MVP)

Smalls Bot is an **authorization-first, AI-assisted security automation scaffold** for educational labs and approved penetration tests.

> ⚠️ This MVP intentionally ships with defensive guardrails and non-offensive defaults. It does not provide exploit automation.

## What is included

- CLI entrypoint (`smalls-bot`) for running workflows from a policy file.
- Workflow engine with step-by-step orchestration and agent hand-offs.
- Agent registry for pluggable specialized agents.
- Async in-memory job queue and worker loop.
- Open-source-friendly LLM abstraction with local/Ollama and OpenAI-compatible adapters.
- Dockerfile and `.env.example` for local startup.

## Legal and ethical use

FOR EDUCATIONAL AND AUTHORIZED TESTING ONLY.

You must only test systems you own or have explicit written authorization to test.

## Quickstart

```bash
cd smalls-bot
python -m venv .venv
source .venv/bin/activate
pip install -e .
smalls-bot run --target https://example.org --authorization-file ./authorization.txt
```

## MVP workflow

1. Authorization validation
2. Passive reconnaissance planning
3. Findings triage
4. Human-review report generation

## Roadmap

- Redis-backed distributed queue
- Multi-worker execution
- Web dashboard with live job feed
- Vector memory and retrieval
