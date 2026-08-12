from __future__ import annotations

import pytest
from unittest.mock import AsyncMock

from docs.kafka_topic_locator import KafkaTopicLocator, MCPCatalogConnector

@pytest.mark.asyncio
async def test_kafka_topic_locator() -> None:
    """Tests the KafkaTopicLocator's ability to locate a Kafka topic."""

    # Arrange
    mocked_connector = AsyncMock(spec=MCPCatalogConnector)
    mocked_connector.search_data = AsyncMock(return_value=[{"id": "1234"}])
    mocked_connector.get_data_details = AsyncMock(return_value={"name": "test-topic"})

    topic_locator = KafkaTopicLocator("test-topic", mocked_connector)

    # Act
    topic_details = await topic_locator.locate_topic()

    # Assert
    assert topic_details == {"name": "test-topic"}
    mocked_connector.search_data.assert_called_once_with("test-topic")
    mocked_connector.get_data_details.assert_called_once_with("1234")
