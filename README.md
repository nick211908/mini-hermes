# Mini Hermes

Mini Hermes is a lightweight AI agent framework for building tool-enabled assistants with persistent memory and session recall.

## Overview

This project provides a minimal Hermes-style agent architecture using OpenAI chat models and tool calling.

Key components:

- `agent.py`: core `Agent` class orchestrating chat requests, tool execution, and iterative reasoning.
- `tool_call.py`: tool-calling strategies for structured function calls and text-based tool invocation.
- `tool_registry.py`: centralized tool registration with schema-based metadata and handler execution.
- `memory/persistent.py`: simple file-backed user/profile memory stored in `data/Memory.md` and `data/User.md`.
- `memory/session_db.py`: SQLite session store with FTS5 search for recall across past conversations.
- `memory/recall.py`: recall helper that summarizes past sessions relevant to a query.
- `prompt_builder.py`: builds system prompts from memory, skills, and project context.
- `prompt_caching.py`: message caching utilities for chat systems.

## Requirements

- Python 3.13+
- `openai>=2.48.0`
- `tool-calling>=0.0.0`

## Installation

```bash
python -m pip install -e .
```

Or install dependencies directly:

```bash
python -m pip install openai tool-calling
```

## Configuration

The project includes a placeholder `config.yaml` for model, API key, and runtime settings.

Use the `data/` folder for persistent memory files:

- `data/MEMORY.md`
- `data/USER.md`

## Usage

The agent is designed to be composed with an OpenAI client, a tool registry, and a prompt system.

Example:

```python
from openai import OpenAI
from agent import Agent
from tool_registry import registry
from prompt_builder import PromptBuilder

client = OpenAI(api_key="YOUR_API_KEY")
model = "gpt-4o-mini"

prompt = PromptBuilder().build(
    memory_block="",
    skill_index="",
    user_context="Project context here"
)

agent = Agent(
    client=client,
    model=model,
    system_prompt=prompt,
    tools=registry.get_schemas(),
    tool_handler=registry,
)

response = agent.run("Analyze the project and suggest next improvements.")
print(response)
```

## Tool Registration

Register new tools with `tool_registry.registry.register`:

```python
registry.register(
    name="terminal",
    description="Execute a shell command and return stdout + stderr.",
    parameters={
        "type": "object",
        "properties": {
            "command": {"type": "string"},
            "timeout": {"type": "integer", "default": 30}
        },
        "required": ["command"],
    },
    handler=run_terminal,
)
```

## Notes

This project is a prototype framework and may contain placeholder modules (`cli.py`, `config.yaml`, `tools/file_tools.py`, `tools/memory_tool.py`). It is suited for experimentation and extension into a full tool-enabled assistant platform.
