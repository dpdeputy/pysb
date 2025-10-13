"""Tests for the simple ADK agent."""
from adk_agent.agent import Agent


def test_agent_run():
    """Tests that the agent runs and returns the correct message."""
    agent = Agent()
    assert agent.run() == "Agent is running."
