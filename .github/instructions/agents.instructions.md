```instructions
---
applyTo: "katalon-knowledge-agent/src/agent/**/*.py"
description: "Agent architecture and implementation conventions for Katalon Knowledge Agent"
---
# Agent Architecture (katalon-knowledge-agent)

## Purpose
The Katalon Knowledge Agent is an ADK-based agent that provides information about Katalon products. It serves as:
- A knowledge base agent accessible via A2A protocol
- A UI-integrated agent via ag-ui endpoint
- A specialized retrieval agent for Katalon product documentation

## Agent Roles

### Knowledge Retrieval Agent (Primary)
- Answers questions about Katalon products (TestOps, Studio, TrueTest, etc.)
- Refuses non-Katalon questions to maintain focus
- Uses public MCP server for documentation search
- Provides accurate, factual information from indexed knowledge base

### A2A Integration
- Exposes agent capabilities via Agent-to-Agent protocol
- Can be called by other agents (e.g., Kai Orchestrator Agent)
- Provides agent card for capability discovery
- Supports streaming responses

## Module Structure

### `src/agent/config.py`
- `get_system_prompt(context)`: Generates agent instruction
- `get_agent_config()`: Loads configuration from environment variables
- `get_agent_card(base_url)`: Creates AgentCard for A2A discovery
- All configuration via env vars (no hardcoded values)

### `src/agent/implementation.py`
- `create_agent()`: Main agent creation function
- Configures MCP toolset with StreamableHTTPConnectionParams (public server)
- Creates LlmAgent with MCP tools only
- Wraps in ADKAgent for UI integration
- Returns both LlmAgent (for A2A) and ADKAgent (for UI)

## Configuration Requirements

### Environment Variables
```bash
# Required
AGENT_NAME=katalon_knowledge_agent
MODEL_NAME=gemini-2.5-flash
MCP_PUBLIC_SERVER_URL=https://mcp.qa.katalon.com/mcp

# A2A Configuration
A2A_AGENT_DESCRIPTION=An agent that provides information about Katalon products.
A2A_AGENT_VERSION=1.0.0

# Server Configuration
HOST=0.0.0.0
PORT=8006

# Optional (with defaults)
LOG_LEVEL=INFO
```

## System Prompt Design

### Core Principles
1. **Focused**: Only Katalon product information
2. **Factual**: Information from indexed documentation only
3. **Helpful**: Clear, accurate responses
4. **Boundary-Aware**: Refuse non-Katalon questions

### Scope
- Answer questions about Katalon TestOps, Studio, TrueTest, etc.
- Use MCP tools to search and retrieve documentation
- Do not answer questions outside Katalon products
- Do not hallucinate or make up information

## Agent Lifecycle

1. **Startup**: Load config → Create MCP connection → Initialize LlmAgent → Wrap in ADKAgent
2. **A2A Request**: Direct to LlmAgent via A2A endpoint
3. **UI Request**: Through ADKAgent via ag-ui endpoint
4. **Shutdown**: Automatic cleanup via framework

## A2A Configuration

### Agent Card
Exposes agent metadata for discovery:
- **name**: Unique agent identifier
- **url**: Base URL + `/a2a` path
- **description**: Human-readable capability description
- **version**: Semantic version
- **capabilities**: `{"streaming": True}`
- **skills**: Empty (no predefined skills)
- **modes**: text/plain input and output

### Endpoint Structure
- `/a2a/.well-known/agent-card.json`: Agent card discovery
- `/a2a/task`: Task submission endpoint
- `/ag-ui`: UI integration endpoint (ADK format)

## Testing Strategy

### Unit Tests
- `test_config.py`: Configuration loading, agent card creation
- `test_implementation.py`: Agent creation with mocked MCP

### Integration Tests
- Mock MCP server responses
- Verify A2A agent card format
- Test agent refusal of non-Katalon questions
- Verify streaming capability

## Extension Points

### Adding New Knowledge Sources
1. Add new MCP server connection (if different source)
2. OR add new tools to existing MCP server
3. No agent code changes needed (auto-discovery)
4. Update system prompt if needed

### Changing Agent Scope
1. Update `get_system_prompt()` with new boundaries
2. Update `A2A_AGENT_DESCRIPTION` in config
3. Update agent card version
4. Test with boundary cases

## Performance Considerations
- MCP connections reused across requests
- Database-backed sessions for multi-request context
- Streaming responses for better UX
- Async operations for non-blocking calls

## Security Guidelines
- No authentication required (public knowledge)
- Rate limiting handled at infrastructure level
- Sanitize logs to avoid exposing user queries unnecessarily
- Use HTTPS for production MCP endpoints

## A2A Communication

### As Callable Agent
When called by other agents (e.g., Kai Orchestrator):
1. Receives task via A2A protocol
2. Processes with MCP tools
3. Returns structured response
4. Maintains session context if needed

### Agent Card Updates
When updating agent capabilities:
1. Update `get_agent_card()` with new metadata
2. Increment version number
3. Update description if capability changes
4. Test agent card accessibility

## Maintenance

### When Config Changes
- Update `.env.defaults` with new variables
- Update `.env.example` with commented examples
- Update `get_agent_config()` to load new values
- Update agent card version if public semantics change
- Update this instruction file

### When System Prompt Changes
- Keep prompt in `get_system_prompt()` function
- Document new boundaries/capabilities
- Test with edge cases
- Update agent card description if needed
- Increment agent version

## Future Considerations
- Custom SDK customizations are now in `src/custom_sdk/` for easier maintenance
- Add caching for frequently asked questions
- Implement feedback loop for answer quality
- Add telemetry for popular topics
- Support multiple languages (if knowledge base supports it)

## Differences from Kai Orchestrator Agent
- **No authentication**: Public knowledge, no auth needed
- **Single toolset**: Only MCP public server (no remote agents)
- **A2A primary**: Designed to be called by other agents
- **Simpler scope**: Knowledge retrieval only, no orchestration
- **Starlette vs FastAPI**: Uses Starlette for A2A compatibility

```
