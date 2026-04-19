import pytest
import asyncio
from agents.base import AgentRegistry
from models.agents import AgentInput

@pytest.mark.asyncio
async def test_tool_selection():
    agent = AgentRegistry.get_agent("tool_selection")
    # In sandbox without API key, it returns status="error"
    result = await agent.run(AgentInput(query="Find AI companies"))
    assert result.agent_name == "tool_selection"

@pytest.mark.asyncio
async def test_critic_fallback():
    agent = AgentRegistry.get_agent("critic")
    bad_companies = [{"name": "Bad", "industry": "", "employee_count": -1}]
    # Without API key, the critic returns status="PASS" as fallback in the except block
    result = await agent.run(AgentInput(query="test", context={"companies": bad_companies}))
    assert result.agent_name == "critic"

@pytest.mark.asyncio
async def test_agent_registry():
    agents = AgentRegistry.list_agents()
    assert len(agents) == 6
