from __future__ import annotations

import pytest
from src.data_catalog.kafka_topic_search import search_kafka_topics

def test_search_kafka_topics() -> None:
    # Test the search function
    query = "example_topic"
    result = search_kafka_topics(query)
    assert isinstance(result, dict)
