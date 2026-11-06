# 01 — OpenAI Agents SDK Quickstart

Two small experiments based on the official SDK quickstart.

## Experiments

1. `01_basic_agent.py`: create an `Agent`, run it with `Runner`, read `final_output`.
2. `02_tool_calling.py`: register a Python function as a tool; let the model request order data.

Both scripts require `OPENAI_API_KEY` and use an API call. Check OpenAI Dashboard traces to see whether and when the tool was invoked.

## Questions to investigate

- What does the model decide versus what does Python execute?
- Does the tool call occur on every run?
- What changes when the tool description is more explicit?

Record actual observations in `learning-notes.md` after running.
