```instructions
---
applyTo: "katalon-knowledge-agent/README.md"
description: "Concise README and developer doc style standard for katalon-knowledge-agent"
---
# Documentation Standard (katalon-knowledge-agent)

**CRITICAL**: All documentation changes must follow the same principle as public-mcp-server. Any change to code, architecture, or configuration requires updates to README + ALL relevant .github/ files in the same PR.

Goal: Keep documentation minimal, fast to scan, and code-navigation oriented. The README should enable a new developer to run the agent, understand its A2A integration, and locate source files—without duplicating inline code metadata.

## Core Sections (Order)
1. Title & one-line purpose
2. Prerequisites (Python version, tooling, external services)
3. Quick Start (install + run in <= 6 commands)
4. Agent capabilities (high-level description)
5. A2A Integration (agent card, endpoints)
6. Configuration (environment vars with defaults + overrides explanation)
7. Deployment (Docker, production command, health check)
8. Architecture (brief modular structure overview)
9. Navigation (pointer list of key files & their roles)
10. Development (reference to development-workflow.instructions.md)
11. Troubleshooting (5-8 focused bullets)
12. Notes / references to deeper standards

## Style Rules
- Sentences: Prefer imperative, concise (<120 chars each)
- Avoid marketing language; focus on behavior and location
- Do not copy environment variable details—keep those in .env.defaults
- Use fenced code blocks for commands; one logical task per block
- Keep README < ~300 lines; aim < 250 lines
- Prefer bullet lists; avoid long paragraphs (>3 sentences)
- Link to instruction files rather than restating conventions

## Agent Capabilities Section
- Describe what the agent does at a high level
- Mention Katalon product focus
- List MCP server integration
- Keep to 3-5 bullet points

## A2A Integration Section
- Explain agent card endpoint
- Show example agent card JSON
- List available endpoints (A2A, ag-ui)
- Mention how other agents can call this agent
- Keep to 5-8 bullet points

## Configuration Section
- Explain `.env.defaults` (default values) and `.env` (overrides)
- Show only required + commonly optional vars
- Reference `.env.example` for full list
- No secrets examples

## Architecture Section
- Brief overview of modular structure
- Explain dual agent return (LlmAgent + ADKAgent)
- Mention Starlette app with A2A endpoint
- Keep to 3-5 bullet points

## Navigation Section
- Each line: `path` – role summary in 3-8 words
- Include: `src/main.py`, `src/server.py`, `src/agent/`, `src/shared/`, `src/custom_sdk/`
- Exclude transient directories (`__pycache__`, `venv/`)

## Development Section
- Reference development-workflow.instructions.md for commands
- Brief mention of test structure
- Link to agents.instructions.md for architecture details

## Troubleshooting Patterns
Use concise bullet symptom → action format:
- "Agent not starting" → check env vars in `.env.defaults`
- "MCP connection failed" → check MCP server URL and availability
- "Agent card not accessible" → verify `/a2a/.well-known/agent-card.json` endpoint
- "A2A calls failing" → check agent card URL in calling agent
- "Import errors" → ensure `uv sync --locked` was run

## Anti-Patterns
- Duplicating configuration documentation
- Embedding full system prompt in README
- Including long architectural diagrams
- Mixing deployment script details
- Hardcoding configuration values in docs
- Explaining A2A protocol details (link to spec instead)

## Maintenance
- Update README when public semantics, run commands, or dependency workflow changes
- uv is the mandatory dependency manager; do not add pip instructions
- After any config or agent change: update README + relevant instruction files in the same PR
- Keep instruction files authoritative for deep conventions
- Update Architecture section if module structure changes
- Update A2A section if agent card format changes

## A2A-Specific Documentation
- Always mention agent card endpoint first
- Show example curl command to get agent card
- Explain how to call agent from another agent
- Document streaming support
- Link to A2A protocol specification if available

This standard ensures developers ramp quickly while code remains the single source of truth for detailed semantics. The modular architecture makes the agent maintainable and extensible. Using uv guarantees reproducible, cached installs and consistent dev tooling.

```
