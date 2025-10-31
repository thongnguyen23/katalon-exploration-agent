````instructions
---
applyTo: "katalon-knowledge-agent/**/*"
description: "Local development workflow: standardized commands for lint, format, type-check, test, run"
---
# Development Workflow (katalon-knowledge-agent)

Use `uv` for all runtime/test commands and `uvx` for ephemeral tooling. Never invoke tools directly if a `uv run` or `uvx` variant exists.

## Core Commands

```bash
# Install (dev + lock enforcement)
uv sync --all-extras --dev

# Run server (entry point defined in pyproject [project.scripts])
uv run katalon-knowledge-agent

# Type checking
uv run pyright

# Lint (Ruff)
uvx ruff check

# Format (Ruff formatter)
uvx ruff format
# Verify formatting only (CI style)
uvx ruff format --check

# Tests (entire suite)
uv run pytest -q
# Tests (verbose, specific module)
uv run pytest tests/ -v
uv run pytest tests/ -k "test_config"
```

## Pre-Commit Checklist
1. `uv sync --locked` (ensure reproducible deps)
2. `uvx ruff check` (lint must pass)
3. `uvx ruff format --check` (formatting clean)
4. `uv run pyright` (types ok)
5. `uv run pytest -q` (tests green)
6. Update README + relevant `.github/instructions/` if semantics changed
7. Add/adjust tests for new or changed behavior

## Logging Consistency
- Use per-module `logger = logging.getLogger(__name__)`
- Central format set in `src/server.py`
- No direct `logging.info()` calls without module-scoped logger

## Adding Dependencies
```bash
uv add <package>          # runtime
uv add --dev <package>    # dev
uv remove <package>
uv lock                   # (implicit on add/remove)
```
Commit updated `pyproject.toml` and lock artifacts every time.

## Configuration Management
- All config values in `.env.defaults` with defaults
- User overrides in `.env` file (gitignored)
- Load config once at startup via `src/shared/config.py::load_config()`
- Access via `get_env()`, `get_env_int()`, `get_env_bool()`
- No hardcoded constants; everything configurable

## Troubleshooting Quick Commands
```bash
# Health check
curl http://localhost:8006/health

# Environment check
uv run python -c "import os; from dotenv import load_dotenv; load_dotenv('.env.defaults'); print(os.getenv('AGENT_NAME'))"

# Test agent connection to MCP server
curl -v <MCP_PUBLIC_SERVER_URL>

# Check A2A agent card
curl http://localhost:8006/a2a/.well-known/agent-card.json
```

## CI Parity
Ensure local run mirrors CI:
- CI uses `uv sync --locked`
- CI runs: `uvx ruff check`, `uvx ruff format --check`, `uv run pyright`, `uv run pytest`

## Module Structure
```
src/
├── __init__.py              # Package exports
├── main.py                  # Entry point
├── server.py                # Starlette app setup with A2A endpoint
├── agent/                   # Agent implementation
│   ├── __init__.py
│   ├── config.py           # Agent configuration + AgentCard
│   └── implementation.py   # Agent creation logic
└── shared/                  # Shared utilities
    ├── __init__.py
    ├── config.py           # Configuration helpers
    ├── types.py            # Shared type definitions
    └── utils.py            # Utility functions
```

Following these steps guarantees consistent quality gates and reproducibility across contributors.

````
