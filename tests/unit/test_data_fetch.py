import pytest
from unittest.mock import MagicMock
from src.data_catalog.data_fetch import fetch_kafka_topics, MockMcpClient

@pytest.fixture
def mock_mcp_client():
    client = MagicMock(spec=MockMcpClient)
    client.search_data.return_value = ["topic_1", "topic_2"]
    client.get_data_details.side_effect = lambda identifier: {"id": identifier, "details": f"Details for {identifier}"}
    return client

def test_fetch_kafka_topics_filtering(mock_mcp_client, monkeypatch):
    monkeypatch.setattr("src.data_catalog.data_fetch.MockMcpClient", lambda: mock_mcp_client)

    filter_pattern = "topic_"
    expected_result = [
        {"id": "topic_1", "details": "Details for topic_1"},
        {"id": "topic_2", "details": "Details for topic_2"}
    ]

    result = fetch_kafka_topics(filter_pattern)
    assert result == expected_result
    mock_mcp_client.search_data.assert_called_once_with(filter_pattern)
    assert mock_mcp_client.get_data_details.call_count == len(expected_result)

def test_fetch_kafka_topics_no_matches(mock_mcp_client, monkeypatch):
    monkeypatch.setattr("src.data_catalog.data_fetch.MockMcpClient", lambda: mock_mcp_client)

    mock_mcp_client.search_data.return_value = []

    filter_pattern = "nonexistent"
    expected_result = []

    result = fetch_kafka_topics(filter_pattern)
    assert result == expected_result
    mock_mcp_client.search_data.assert_called_once_with(filter_pattern)
    assert mock_mcp_client.get_data_details.call_count == 0