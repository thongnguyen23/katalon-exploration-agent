"""Workflow registries for building agent instances used by the runtime."""

from a2a.types import AgentCard
from ag_ui_adk import ADKAgent
from google.adk.agents import LlmAgent

from ..agent import create_agent, get_agent_card


def build_primary_agent(base_url: str) -> tuple[LlmAgent, ADKAgent, AgentCard]:
    """Build the primary agent and associated agent card used by ag-ui.

    Args:
        base_url: Base URL used to construct the AgentCard URL

    Returns:
        Tuple of (LlmAgent, ADKAgent, AgentCard)
    """
    llm_agent, adk_agent = create_agent()
    agent_card = get_agent_card(base_url)
    return llm_agent, adk_agent, agent_card

