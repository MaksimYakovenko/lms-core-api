from __future__ import annotations

from search_kafka_topic import locate_kafka_topic_details
from mcp import search_data, get_data_details
import pytest

def test_locate_kafka_topic_details(monkeypatch) -> None:
    """Test the locate_kafka_topic_details function."""
    def mock_search_data(criteria):
        if criteria["name"] == "epm-skls-ai.courses-to-take":
            return [{"id": "topic1234", "name": "epm-skls-ai.courses-to-take"}]
        return []

    def mock_get_data_details(data_id):
        if data_id == "topic1234":
            return {"id": "topic1234", "details": "Some details"}
        return {}
    
    monkeypatch.setattr("mcp.search_data", mock_search_data)
    monkeypatch.setattr("mcp.get_data_details", mock_get_data_details)

    topic_name = "epm-skls-ai.courses-to-take"
    result = locate_kafka_topic_details(topic_name)
    assert result == {"id": "topic1234", "details": "Some details"}
