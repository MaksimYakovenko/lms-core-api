from __future__ import annotations

import pytest
import asyncio
from src.data_catalog.entity_search import query_kafka_topic

@pytest.mark.asyncio
def test_query_kafka_topic(dummy_data_catalog) -> None:
    topic_name = "test-topic"
    expected_result = {"name": "test entity", "type": "test-type". "project": "test-project"}
    result = asyncio.run(query_kafka_topic(topic_name))
    assert result == expected_result
    expected_empty_result = None
    empty_result = asyncio.run(query_kafka_topic("non-existent-topic"))
    assert empty_result == expected_empty_result
