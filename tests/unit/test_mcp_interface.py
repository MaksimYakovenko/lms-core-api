import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from src.service.mcp_interface import McpService

@pytest.mark.asyncio
async def test_search_data_entity_found():
    # Test the McpService's search_data method when an entity is found in the database
    mcp_service = McpService(kafka_topic="test-topic", db_url="postgresql://localhost/test_db")

    # Mock the database pool and connection
    mcp_service.db_pool = AsyncMock()
    mock_connection = AsyncMock()
    mcp_service.db_pool.acquire.return_value.__aenter__.return_value = mock_connection

    # Mock the database fetch result
    mock_fetch_result = [{"data": "{'field': 'value'}"}]
    mock_connection.fetch.return_value = mock_fetch_result

    # Call search_data and assert the return value
    result = await mcp_service.search_data("identifier")
    assert result == [{"data": "{'field': 'value'}"}]
    mock_connection.fetch.assert_called_with(
        """
                SELECT data
                FROM records
                WHERE identifier = $1
            """, "identifier"
    )

@pytest.mark.asyncio
async def test_search_data_no_entity_found():
    # Test the McpService's search_data method when no entity is found in the database
    mcp_service = McpService(kafka_topic="test-topic", db_url="postgresql://localhost/test_db")

    # Mock the database pool and connection
    mcp_service.db_pool = AsyncMock()
    mock_connection = AsyncMock()
    mcp_service.db_pool.acquire.return_value.__aenter__.return_value = mock_connection

    # Mock the database fetch result
    mock_connection.fetch.return_value = []

    # Call search_data and assert the return value
    result = await mcp_service.search_data("identifier")
    assert result == []

@pytest.mark.asyncio
async def test_process_topic_entities():
    # Test the McpService's process_topic_entities method

    mcp_service = McpService(kafka_topic="test-topic", db_url="postgresql://localhost/test_db")

    # Mock methods
    mcp_service.search_data = AsyncMock(return_value=[{"data": "{'field': 'value'}"}])

    # Mock the Kafka consumer
    mock_kafka_consumer = MagicMock()
    mock_kafka_consumer.__iter__.return_value = [{"key": b"identifier"}]

    with patch("src.service.mcp_interface.KafkaConsumer", return_value=mock_kafka_consumer):
        # Call process_topic_entities
        await mcp_service.process_topic_entities()

        # Assert search_data was called
        mcp_service.search_data.assert_called_with("identifier")