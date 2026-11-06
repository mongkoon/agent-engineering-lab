# Agent Engineering Lab

**Language:** [English](README.md) | [한국어](README.ko.md)

Hands-on AI agent engineering experiments: from OpenAI Agents SDK fundamentals to a reliable commerce customer support agent.

## Status

- `01-quickstart/` — Starter examples (not yet executed against a live LLM API)
- `02-commerce-cs-agent/` — Planned MVP; implementation will be added incrementally

## Learning path

| Stage | Focus | Evidence |
| --- | --- | --- |
| 01 | Agent / Runner / function tools | Executable scripts and learning notes |
| 02 | Tool calling, state, human approval, error recovery, evaluation | Commerce CS Agent with test results |

## Quick start

Requires Python 3.11+ and an OpenAI API key with API billing enabled.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY='your-api-key' # Set locally; never commit secrets
python 01-quickstart/01_basic_agent.py
python 01-quickstart/02_tool_calling.py
```

These examples make paid API requests. Review model selection and budget controls in your OpenAI API account before running.

## Official references

- [OpenAI Agents SDK Quickstart](https://openai.github.io/openai-agents-python/quickstart/)
- [OpenAI Agents SDK Tools](https://openai.github.io/openai-agents-python/tools/)

## Security

This repository uses fictional data only. Keep API keys, local database files, and unredacted traces out of Git.

## Notes

Implementation results and measured outcomes will be added only after local runs. No production deployment or evaluation success is claimed.
