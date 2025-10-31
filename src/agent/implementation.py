"""Agent implementation for Katalon Knowledge Agent."""

import logging

from ag_ui_adk import ADKAgent
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from google.adk.models.lite_llm import LiteLlm


from .config import get_agent_config, get_system_prompt

logger = logging.getLogger(__name__)


def create_agent() -> tuple[LlmAgent, ADKAgent]:
    """Create and configure the Katalon Knowledge Agent.
    
    Returns:
        Tuple of (LlmAgent, ADKAgent) instances
    """
    config = get_agent_config()
    
    # Configure MCP server connection
    mcp_public_server = StreamableHTTPConnectionParams(
        url=config["mcp_server_url"],
    )
    
    # Create LiteLLM model wrapper for AI models
    model = LiteLlm(
        model=config["model"],
    )
    
    # Create LLM agent with MCP tools
    llm_agent = LlmAgent(
        name=config["name"],
        instruction=get_system_prompt,
        model=model,
        tools=[
            McpToolset(connection_params=mcp_public_server),
        ],
    )
    
    # Wrap in ADK agent middleware
    adk_agent = ADKAgent(
        adk_agent=llm_agent,
        use_in_memory_services=False,
    )
    
    logger.info(f"Created Katalon Knowledge Agent: {config['name']}")
    
    return llm_agent, adk_agent
