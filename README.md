# Katalon Knowledge Agent

ADK-based knowledge retrieval agent for Katalon product information, with A2A integration.

## Prerequisites

- **Python**: >= 3.12
- **uv**: Fast Python package manager ([install guide](https://docs.astral.sh/uv/))
- **External Services**:
  - Katalon Public MCP Server (documentation search)

## Quick Start

```bash
# Install dependencies
uv sync --all-extras --dev

# Configure (copy and edit .env from .env.example)
cp .env.example .env

# Run server
uv run katalon-knowledge-agent
```

Server starts at `http://localhost:8006` by default.

Health check: `curl http://localhost:8006/health`

Agent card: `curl http://localhost:8006/a2a/.well-known/agent-card.json`

## Agent Capabilities

- **Knowledge Retrieval**: Answers questions about Katalon products (TestOps, Studio, TrueTest, etc.)
- **MCP Integration**: Searches public documentation via MCP server
- **A2A Protocol**: Callable by other agents (e.g., Kai Orchestrator Agent)
- **UI Integration**: Supports ag-ui endpoint for direct user interaction
- **Focused Scope**: Refuses non-Katalon questions

## A2A Integration

This agent exposes Agent-to-Agent (A2A) protocol endpoints:

### Agent Card
```bash
curl http://localhost:8006/a2a/.well-known/agent-card.json
```

Example response:
```json
{
  "name": "katalon_knowledge_agent",
  "url": "http://localhost:8006/a2a",
  "description": "An agent that provides information about Katalon products.",
  "version": "1.0.0",
  "capabilities": {"streaming": true},
  "skills": [],
  "defaultOutputModes": ["text/plain"],
  "defaultInputModes": ["text/plain"]
}
```

### Endpoints
- `/a2a/.well-known/agent-card.json` – Agent card discovery
- `/a2a/task` – Task submission endpoint
- `/ag-ui` – UI integration endpoint (ADK format)
- `/health` – Health check

### Calling from Another Agent
```python
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

katalon_agent = RemoteA2aAgent(
    name="katalon_knowledge_agent",
    agent_card="http://localhost:8006/a2a/.well-known/agent-card.json",
)
```

## Configuration

Configuration loads from `.env.defaults` (defaults) and `.env` (overrides).

### Required Variables
```bash
AGENT_NAME=katalon_knowledge_agent
MODEL_NAME=gemini-2.5-flash
MCP_PUBLIC_SERVER_URL=https://mcp.qa.katalon.com/mcp
```

### A2A Configuration
```bash
A2A_AGENT_DESCRIPTION=An agent that provides information about Katalon products.
A2A_AGENT_VERSION=1.0.0
```

### Optional Variables
```bash
HOST=0.0.0.0         # Server host
PORT=8006            # Server port
LOG_LEVEL=INFO       # Logging level
```

See `.env.example` for full list with comments.

## Deployment

### Local Development
```bash
uv run katalon-knowledge-agent
```

### Production
```bash
# With custom config
HOST=0.0.0.0 PORT=8006 uv run katalon-knowledge-agent
```

### Health Check
```bash
curl http://localhost:8006/health
# Expected: {"status": "healthy", "service": "katalon-knowledge-agent"}
```

## Architecture

- **Modular Structure**: Separate agent logic, server setup, shared utilities
- **Dual Interface**: A2A endpoint (LlmAgent) + ag-ui endpoint (ADKAgent)
- **Starlette App**: Lightweight ASGI app for A2A compatibility
- **MCP Toolset**: Public documentation search only
- **Database Sessions**: Persistent state across requests (`use_in_memory_services=False`)

## Navigation

- `src/main.py` – Entry point, runs uvicorn server
- `src/server.py` – Starlette app, A2A + ag-ui endpoints
- `src/agent/config.py` – Agent config loading, system prompt, agent card
- `src/agent/implementation.py` – Agent creation, returns LlmAgent + ADKAgent
- `src/shared/config.py` – Config helpers (get_env, etc.)
- `src/shared/types.py` – Shared type definitions
- `src/custom_sdk/` – Custom SDK customizations for A2A and ADK endpoints
- `.env.defaults` – Default configuration values
- `.env.example` – Configuration template

## Development

See [development-workflow.instructions.md](.github/instructions/development-workflow.instructions.md) for:
- Core commands (lint, format, type-check, test)
- Pre-commit checklist
- Dependency management
- Troubleshooting

See [agents.instructions.md](.github/instructions/agents.instructions.md) for:
- Agent architecture details
- A2A integration specifics
- System prompt design
- Testing strategy

## Troubleshooting

- **Agent not starting** → Verify `.env` file exists and required vars are set
- **MCP connection failed** → Check MCP_PUBLIC_SERVER_URL and server availability
- **Agent card not accessible** → Verify server is running and `/a2a/.well-known/agent-card.json` is accessible
- **A2A calls failing** → Check agent card URL in calling agent matches deployed URL
- **Import errors** → Run `uv sync --locked` to install dependencies
- **Port conflict** → Change PORT in `.env` to available port

## Notes

- Uses **uv** for dependency management (no pip/poetry)
- Configuration via environment variables only (no hardcoded values)
- **No authentication** required (public knowledge agent)
- System prompt enforces Katalon product focus
- Custom SDK customizations in `src/custom_sdk/` for ADK/A2A compatibility
- Designed to be called by Kai Orchestrator Agent

For detailed conventions, see `.github/instructions/` directory.
