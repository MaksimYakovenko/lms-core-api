from __future__ import annotations

# Unit test for the functionality in data_fetch.py

def test_fetch_kafka_topics() -> None:
    """Test case for fetch_kafka_topics function."""
    from src.data_catalog.data_fetch import fetch_kafka_topics
    filter_pattern = "test"
    topics = fetch_kafka_topics(filter_pattern)
    assert isinstance(topics, list)
    assert len(topics) >= 0
    for topic in topics:
        assert "id" in topic
        assert "details" in topic
