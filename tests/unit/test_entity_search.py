from __future__ import annotations

import pytest
from src.data_catalog.entity_search import locate_entity

def test_locate_entity_found() -> None:
    """Test locate_entity returns the correct entity details."""
    # Mock Kafka topic corresponding to expected data
    kafka_topic = "test-kafka-topic"
    result = locate_entity(kafka_topic)
    assert isinstance(result, dict)
    assert result.get("id") == "entity-123"
    assert "details" in result

def test_locate_entity_not_found() -> None:
    """Test locate_entity returns an error when entity not found."""
    # Mock Kafka topic that doesn't match
    kafka_topic = "nonexistent-topic"
    result = locate_entity(kafka_topic)
    assert isinstance(result, dict)
    assert result.get("error") == "Entity not found"
