from __future__ import annotations

import pytest
import asyncio
from unittest.mock import AsyncMock, patch
from src.data_catalog.entity_search import query_kafka_topic

@pytest.mark.asyncio
async def test_query_kafka_topic() -> None:
    topic_name = "test-topic"
    expected_result = {"name": "test entity", "type": "test-type", "project": "test-project"}
    # Patch DataCatalog
    with patch("src.data_catalog.entity_search.DataCatalog") as MockCatalog:
        mock_catalog = MockCatalog.return_value
        mock_catalog.search_data = AsyncMock(return_value=[expected_result])

        result = await query_kafka_topic(topic_name)
        assert result == expected_result

        mock_catalog.search_data.assert_called_once_with(
            "SELECT * FROM public.entities WHERE topic_name=$1 LIMIT 1;", (topic_name,)
        )

    empty_topic_name = "non-existent-topic"
    expected_empty_result = None
    with patch("src.data_catalog.entity_search.DataCatalog") as MockCatalog:
        mock_catalog = MockCatalog.return_value
        mock_catalog.search_data = AsyncMock(return_value=[])

        result = await query_kafka_topic(empty_topic_name)
        assert result == expected_empty_result

        mock_catalog.search_data.assert_called_once_with(
            "SELECT * FROM public.entities WHERE topic_name=$1 LIMIT 1;", (empty_topic_name,)
        )
