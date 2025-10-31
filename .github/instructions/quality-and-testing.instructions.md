````instructions
---
applyTo: "katalon-knowledge-agent/src/**/*.py"
description: "Quality, testing, and resilience guidelines for agent implementation"
---
# Quality & Testing Standards (katalon-knowledge-agent)

## Design Principles
- Single responsibility per module
- Separation of concerns:
  - `config.py` - Configuration loaders, agent card creation
  - `implementation.py` - Agent creation logic
  - `server.py` - Starlette app, A2A endpoint, middleware
  - `main.py` - Entry point only
- All configuration via environment variables (no hardcoded values)
- Fail fast on missing required configuration
- Support both A2A and UI integration

## Module Structure
```
src/
├── __init__.py              # Package exports
├── main.py                  # Entry point (minimal)
├── server.py                # Starlette app, A2A + ag-ui endpoints
├── agent/                   # Agent implementation
│   ├── __init__.py
│   ├── config.py           # Config loading, prompt, agent card
│   └── implementation.py   # Agent creation logic
└── shared/                  # Shared utilities
    ├── __init__.py
    ├── config.py           # Config helpers (get_env, etc.)
    ├── types.py            # Shared type definitions
    └── utils.py            # Utility functions
```

## Configuration Management
- All config values in `.env.defaults` with defaults
- User overrides in `.env` file (gitignored)
- Load config once at startup via `load_config()`
- Access via `get_env()`, `get_env_int()`, `get_env_bool()` helpers
- Raise `ValueError` for missing required variables

## Validation & Constraints
- Validate environment variables on startup
- Use type-safe config accessors (`get_env_int`, `get_env_bool`)
- Document required vs optional variables in `.env.example`
- Fail fast with clear error messages
- Validate agent card structure

## Resilience
- Wrap external calls (MCP) in try/except if needed
- Log errors with context but don't expose internals
- Use conservative defaults
- Health check endpoint for monitoring (`/health`)
- Graceful handling of MCP connection failures

## Testing Guidelines
Each module should have comprehensive unit tests covering:

### Test Structure
- Location: `tests/` directory mirroring `src/` structure
- Files: `test_config.py`, `test_implementation.py`, `test_server.py`
- Framework: pytest with pytest-asyncio for async support
- Mocking: Use unittest.mock and pytest-mock for external dependencies

### Required Test Coverage
1. **test_config.py** - Configuration loading:
   - Loading from `.env.defaults`
   - Override with `.env` values
   - Required variables (should raise on missing)
   - Type conversions (int, bool, string)
   - System prompt generation
   - Agent card creation with correct structure

2. **test_implementation.py** - Agent creation:
   - Agent creation with valid config
   - MCP toolset initialization
   - LlmAgent creation
   - ADKAgent wrapping
   - Dual return (LlmAgent, ADKAgent)
   - Error handling for missing config

3. **test_server.py** - Server and middleware:
   - Health check endpoint
   - A2A endpoint registration
   - ag-ui endpoint registration
   - Request logging middleware
   - Starlette app creation
   - Agent card accessibility

### A2A-Specific Tests
- Agent card endpoint (`/a2a/.well-known/agent-card.json`)
- Agent card JSON structure validation
- A2A task submission endpoint
- Streaming response support
- Agent card version in responses

### Mocking Strategy
- Mock external dependencies (MCP server)
- Use `patch.dict(os.environ, ...)` for config tests
- Use `AsyncMock` for async external calls
- Verify external calls receive correct parameters
- Test error paths by making mocks raise exceptions
- Mock A2A protocol handlers

### Running Tests
```bash
uv run pytest tests/ -v              # all tests with verbose output
uv run pytest tests/test_config.py   # specific test file
uv run pytest tests/ -k "agent"      # tests matching pattern
uv run pytest tests/ -k "a2a"        # A2A-specific tests
```

### CI Integration
- Tests run automatically on PR
- Uses `uv sync --locked` for reproducible dependencies
- Must pass before merge

## Logging Strategy
- Use module-level logger: `logger = logging.getLogger(__name__)`
- Configure logging in `server.py` (format, level)
- INFO: Major operations (agent creation, request handling)
- DEBUG: Detailed info (headers, bodies) - avoid in production
- ERROR: Exception contexts with module name prefix
- Log A2A task submissions at INFO level

## Security & Privacy
- No authentication for public knowledge agent
- Sanitize user queries in logs if they may contain sensitive info
- Use DEBUG level for full request details
- All configuration via environment variables
- Use HTTPS for production MCP endpoints
- Rate limiting at infrastructure level

## Performance
- Reuse MCP connections (managed by McpToolset)
- Use database-backed sessions (`use_in_memory_services=False`)
- Async operations for external calls
- Streaming responses for better UX
- Health check for monitoring and load balancer integration

## Documentation Coupling
- README describes high-level capabilities and A2A integration
- `.env.example` shows all available configuration
- This instruction file details architecture and testing
- Code comments explain complex logic
- System prompt in code with documentation in agents.instructions.md
- Agent card metadata in config

## Review Checklist (for PRs)
- [ ] Module structure follows standards
- [ ] Configuration uses environment variables
- [ ] `.env.defaults` updated with new variables
- [ ] `.env.example` updated (commented)
- [ ] Agent card structure valid
- [ ] A2A endpoint properly registered
- [ ] Logging doesn't expose sensitive data
- [ ] Tests added/updated for changes
- [ ] A2A tests cover agent card and task endpoints
- [ ] README updated if public semantics changed
- [ ] Instruction files updated if architecture changed
- [ ] `uv sync --locked` works without errors

## Maintenance & Dependency Workflow
- Use `uv add/remove` for dependency changes
- Commit `pyproject.toml` and lock files together
- Update documentation with code changes
- Keep `.env.example` in sync with actual usage
- Test with fresh environment to verify dependencies
- Update agent card version when semantics change

## Agent-Specific Guidelines

### System Prompt Updates
- Keep prompt in `get_system_prompt()` function
- Document prompt purpose in code comments
- Test prompt changes with various user inputs
- Update agents.instructions.md when behavior changes
- Update agent card description if scope changes

### Agent Card Updates
- Version bump for any public semantic change
- Update description for new capabilities
- Test agent card accessibility
- Verify JSON structure matches A2A spec
- Document changes in agents.instructions.md

### Adding MCP Tools
- Tools added at MCP server side (no agent code change)
- Auto-discovery via McpToolset
- Update system prompt if tool needs explanation
- Test with mocked MCP responses

### Middleware Changes
- Keep request logging for debugging
- Consider performance impact
- Test middleware with various request patterns
- Maintain Starlette compatibility for A2A

## A2A Integration Guidelines

### Agent Card Maintenance
- Always validate against A2A spec
- Version bump for breaking changes
- Test card accessibility before deploy
- Document card structure in tests

### Endpoint Testing
- Test both A2A and ag-ui endpoints
- Verify streaming works in both modes
- Test agent card discovery
- Test task submission and response format

### Cross-Agent Testing
- Test being called by other agents (mock caller)
- Verify context propagation
- Test error responses in A2A format
- Validate task completion notifications

Maintain these standards to keep the agent reliable, maintainable, A2A-compliant, and LLM-friendly.

````
