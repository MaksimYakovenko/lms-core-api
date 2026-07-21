from __future__ import annotations

import pytest
from src.data_catalog.entity_search import locate_entity

def test_locate_entity() -> None:
    """Test locate_entity function."""
    # Use a mock Kafka topic
    kafka_topic = "test-kafka-topic"
    result = locate_entity(kafka_topic)
    assert isinstance(result, dict)
