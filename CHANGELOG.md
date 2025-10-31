Changelog — Refactor Only (restructure-kai)

Summary
- Restructured code into modular layout without changing behavior.
- Preserved all public endpoints, import paths, and startup commands.

Moves/Renames
- New: `src/runtime/` — owns FastAPI app and routing
  - Added: `src/runtime/server.py` (moved server logic)
  - Added: `src/runtime/main.py` (moved main entry)
- New: `src/workflows/` — assembly layer for agent instances
  - Added: `src/workflows/registry.py` with `build_primary_agent(base_url)`
- New: `src/interfaces/` — placeholder for shared contracts (no behavior)
- Facades to preserve public imports:
  - `src/server.py` now re-exports `app` and `get_server_config` from `runtime.server`
  - `src/main.py` now delegates to `runtime.main.main`

Unchanged
- `src/agent/` — agent configuration and implementation
- `src/shared/` — environment helpers and utilities
- `src/custom_sdk/` — untouched per spec

Behavioral Parity
- HTTP endpoints, paths, and middleware remain unchanged:
  - `/a2a`, `/ag-ui`, `/health`
- Startup command via `uvicorn src.server:app` remains valid.
- No new configuration keys or runtime behavior introduced.
