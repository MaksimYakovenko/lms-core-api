from __future__ import annotations

from unittest.mock import AsyncMock, patch
import pytest

from service.mcp_interface import McpService

@pytest.mark.asyncio
async def test_search_data():
    """Test searching data in the MCP system."""
    with patch("service.mcp_interface.McpService.db_pool") as mock_pool:
        mock_conn = AsyncMock()
        mock_pool.acquire.return_value.__aenter__.return_value = mock_conn
        mock_conn.fetch.return_value = [
            {"data_key": "data_value"}
        ]
        
        service = McpService(kafka_topic="mock-topic", db_url="mock-db-url")
        
        service.db_pool = mock_pool
        
        result = await service.search_data(identifier="test_identifier")
        assert result == [{"data_key": "data_value"}]

@pytest.mark.asyncio
async def test_process_topic_entities():
    """Test processing entities from Kafka topic."""
    with patch("service.mcp_interface.McpService.search_data") as mock_search:
        mock_search.return_value = [{"data": "example_data"}]
        
        with patch("service.mcp_interface.McpService.subscribe_to_topic", return_value=(i for i in ["test1", "test2"])):
            service = McpService(kafka_topic="mock-topic", db_url="mock-db-url")
            await service.process_topic_entities()
            mock_search.assert_called()

@pytest.fixture
async def mcp_service():
    """Fixture providing initialized instance of McpService."""
    service = McpService(kafka_topic="test-topic", db_url="test-db-url")
    await service.initialize()
    yield service
    await service.terminate()
