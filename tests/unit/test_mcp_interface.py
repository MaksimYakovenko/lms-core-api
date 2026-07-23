from __future__ import annotations

import pytest
from service.mcp_interface import McpService

@pytest.mark.asyncio
async def test_search_data():
    service = McpService(kafka_topic="test-topic", db_url="test-db-url")
    identifier = "test-entity"
    result = await service.search_data(identifier)
    assert result is not None

@pytest.mark.asyncio
async def test_process_topic_entities():
    service = McpService(kafka_topic="test-topic", db_url="test-db-url")
    await service.process_topic_entities()
    assert True
