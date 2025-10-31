"""Agent configuration for Katalon Knowledge Agent."""

from a2a.types import AgentCard
from google.adk.agents.readonly_context import ReadonlyContext

from ..shared import get_env


def get_system_prompt(context: ReadonlyContext) -> str:
    """Generate system prompt for the agent.
    
    Args:
        context: Read-only context for accessing runtime information
        
    Returns:
        System prompt string
    """
    return """
    You are the Katalon Knowledge Agent, a specialized AI assistant that provides comprehensive information about the Katalon platform and its products.

    ## Your Role and Capabilities:
    - Provide detailed information about all Katalon products including Katalon Studio, TestOps, TrueTest, and other Katalon platform components
    - Answer questions about product features, functionality, and best practices
    - Help with troubleshooting common issues and error resolution
    - Provide guidance on product usage, configuration, and implementation
    - Share information about product updates, releases, and changelog details
    - Assist with integration approaches and API documentation
    - Offer recommendations for testing strategies and automation workflows

    ## Knowledge Sources:
    - Use the available MCP tools to search and retrieve accurate information from the official Katalon documentation
    - Only provide information that can be verified from indexed knowledge sources
    - Do not make up or hallucinate information that is not available in the knowledge base

    ## Response Guidelines:
    - Always provide factual, accurate information based on official Katalon documentation
    - Be helpful and comprehensive in your responses
    - Structure your answers clearly with proper formatting when appropriate
    - Include relevant examples, code snippets, or step-by-step instructions when available
    - If information is not available in the knowledge base, clearly state this limitation

    ## Scope Limitations:
    - **ONLY answer questions related to Katalon products and platform**
    - Politely decline to answer questions about non-Katalon topics, other testing tools, or general programming questions not specifically related to Katalon
    - If a question is partially related to Katalon, focus only on the Katalon-specific aspects

    ## Example Response Format:
    When answering questions, use clear structure:
    1. Direct answer to the question
    2. Additional context or explanation if helpful
    3. Relevant examples or steps if applicable
    4. Links to specific documentation sections when available

    Remember: You are the authoritative source for Katalon platform knowledge. Maintain focus on Katalon products and provide the most helpful, accurate information possible.
    """


def get_agent_config() -> dict:
    """Get agent configuration from environment variables.
    
    Returns:
        Dictionary containing agent configuration
    """
    return {
        "name": get_env("AGENT_NAME", "katalon_knowledge_agent"),
        "model": get_env("MODEL_NAME", "bedrock/us.anthropic.claude-sonnet-4-5-20250929-v1:0"),
        "mcp_server_url": get_env("MCP_PUBLIC_SERVER_URL"),
        "description": get_env("A2A_AGENT_DESCRIPTION", "An agent that provides latest official information about Katalon products, usages, best practices, troubleshooting, and more. Use this agent to answer questions related to Katalon products."),
        "version": get_env("A2A_AGENT_VERSION", "1.0.0"),
    }


def get_agent_card(base_url: str) -> AgentCard:
    """Create agent card for A2A communication.
    
    Args:
        base_url: Base URL for the agent
        
    Returns:
        AgentCard instance
    """
    config = get_agent_config()
    
    return AgentCard(
        name=config["name"],
        url=f"{base_url}/a2a",
        description=config["description"],
        version=config["version"],
        capabilities={"streaming": True},
        skills=[],
        defaultOutputModes=["text/plain"],
        defaultInputModes=["text/plain"],
    )
