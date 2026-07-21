from __future__ import annotations

import os
import pytest
from unittest.mock import AsyncMock, patch
from docs.kafka_topic_locator import KafkaTopicLocator

@pytest.mark.asyncio
async def test_locate_and_retrieve_topic_info() -> None:
    """Test the locate_and_retrieve_topic_info function."""

    mock_results = [{"name": os.getenv("KAFKA_TARGET_TOPIC", "epm-skls-ai.courses-to-take"), "id": "12345"}]
    mock_details = {"name": "epm-skls-ai.courses-to-take", "description": "A sample Kafka topic."}

    with patch("mcp_tools.search_data", AsyncMock(return_value=mock_results)) as mock_search, \
         patch("mcp_tools.get_data_details", AsyncMock(return_value=mock_details)) as mock_get:

        locator = KafkaTopicLocator()

        result = await locator.locate_and_retrieve_topic_info()

        assert result == mock_details

        mock_search.assert_called_once_with(os.getenv("KAFKA_TARGET_TOPIC", "epm-skls-ai.courses-to-take"))
        mock_get.assert_called_once_with("12345")
