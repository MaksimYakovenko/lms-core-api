from __future__ import annotations

import pytest
from modules.catalog_locator import CatalogLocator, MCPClient

def test_catalog_locator() -> None:
    """Test locating a catalog entity."""
    kafka_topic = 'epm-skls-ai.courses-to-take'
    mcp_client = MCPClient()
    locator = CatalogLocator(mcp_client=mcp_client, kafka_topic=kafka_topic)
    entity_details = locator.locate()

    assert entity_details['id'] == "1234"
    assert entity_details['name'] == "Entity Details"

def test_catalog_locator_not_found() -> None:
    """Test locating a non-existent catalog entity."""
    kafka_topic = 'non-existent-topic'
    mcp_client = MCPClient()
    locator = CatalogLocator(mcp_client=mcp_client, kafka_topic=kafka_topic)
    with pytest.raises(ValueError):
        locator.locate()
