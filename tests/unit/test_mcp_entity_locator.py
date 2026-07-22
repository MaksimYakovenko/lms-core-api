from __future__ import annotations

import pytest
from src.data_retrieval.mcp_entity_locator import MCPEntityLocator

def test_mcp_entity_locator() -> None:
    """Unit test for the MCPEntityLocator class."""
    topic_name = "epm-skls-ai.courses-to-take"
    locator = MCPEntityLocator(topic_name=topic_name)
    assert locator.locate_entity() == "entity-id-12345"

def test_mcp_entity_locator_not_found() -> None:
    """Unit test for the MCPEntityLocator class with not found scenario."""
    topic_name = "unknown-topic"
    locator = MCPEntityLocator(topic_name=topic_name)
    assert locator.locate_entity() is None
