"""FastAPI server for Katalon Knowledge Agent with A2A support.

Owns HTTP app creation, middleware, and endpoint wiring.
"""

import logging

from ag_ui_adk import add_adk_fastapi_endpoint
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from ..workflows.registry import build_primary_agent
from ..shared import get_env, get_env_int, load_config
from ..custom_sdk.agent_to_a2a import add_a2a_endpoint

# Load configuration from .env files
load_config()

# Configure application-wide logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
)

logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI()

# Get server configuration
host = get_env("HOST", "0.0.0.0")
port = get_env_int("PORT", 8006)
base_url = f"http://{host}:{port}"

# Create agent instances and agent card via workflow registry
llm_agent, adk_agent, agent_card = build_primary_agent(base_url)

# Add A2A endpoint for agent-to-agent communication
add_a2a_endpoint(
    app=app,
    path="/a2a",
    agent=llm_agent,
    agent_card=agent_card,
)

# Add ADK endpoint for UI integration
add_adk_fastapi_endpoint(app, adk_agent, path="/ag-ui")


@app.middleware("http")
async def log_request(request: Request, call_next):
    """Middleware to log incoming requests."""
    # Clone the body since it can be consumed only once
    body_bytes = await request.body()

    # Log useful parts
    logger.info(f"➡️ Request URL: {request.url}")
    logger.info(f"➡️ Method: {request.method}")
    logger.debug(f"➡️ Headers: {dict(request.headers)}")
    logger.debug(f"➡️ Query Params: {dict(request.query_params)}")
    logger.debug(
        f"➡️ Body: {body_bytes.decode('utf-8') if body_bytes else '(empty)'}"
    )

    # Recreate the stream for downstream handlers
    async def receive():
        return {"type": "http.request", "body": body_bytes}

    new_request = Request(request.scope, receive)
    response = await call_next(new_request)
    return response


@app.route("/health")
async def health_check(request):
    """Health check endpoint."""
    return JSONResponse({"status": "healthy", "service": "katalon-knowledge-agent"})


def get_server_config():
    """Get server configuration from environment variables."""
    return {
        "host": get_env("HOST", "0.0.0.0"),
        "port": get_env_int("PORT", 8006),
    }

