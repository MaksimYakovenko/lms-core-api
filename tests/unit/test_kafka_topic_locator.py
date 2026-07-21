import pytest
from unittest.mock import AsyncMock
from docs.kafka_topic_locator import KafkaTopicLocator, MCPCatalogConnector

@pytest.mark.asyncio
async def test_locate_topic_found():
    """Test behavior when the topic is successfully located."""

    # Mock the connector
    mock_connector = MCPCatalogConnector()
    mock_connector.search_data = AsyncMock(return_value=[{'id': 'topic123'}])
    mock_connector.get_data_details = AsyncMock(return_value={'details': 'Topic details'})

    # Instantiate the KafkaTopicLocator
    locator = KafkaTopicLocator('test-topic', mock_connector)

    # Perform the locate_topic action
    result = await locator.locate_topic()

    # Assertions
    assert result == {'details': 'Topic details'}

@pytest.mark.asyncio
async def test_locate_topic_not_found():
    """Test behavior when the topic is not found in search results."""

    # Mock the connector
    mock_connector = MCPCatalogConnector()
    mock_connector.search_data = AsyncMock(return_value=[])

    # Instantiate the KafkaTopicLocator
    locator = KafkaTopicLocator('unknown-topic', mock_connector)

    # Perform the locate_topic action with assertion for exception
    with pytest.raises(ValueError, match="Topic unknown-topic not found."):
        await locator.locate_topic()