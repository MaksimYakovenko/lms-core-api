import pytest
from unittest.mock import patch
from src.data_catalog.kafka_topic_search import search_kafka_topics


def test_search_kafka_topics_found():
    """Verify topics are found based on the query."""
    mock_search_data = [{'id': 'topic1', 'type': 'kafka_topic'}]
    mock_get_data_details = {'id': 'topic1', 'name': 'Topic 1', 'type': 'kafka_topic'}

    with patch('external.mcp_tools.search_data', return_value=mock_search_data) as search_mock,
         patch('external.mcp_tools.get_data_details', return_value=mock_get_data_details) as details_mock:

        result = search_kafka_topics(query="test_query")

        search_mock.assert_called_once_with(query="test_query", search_filter={"type": "kafka_topic"})
        details_mock.assert_called_once_with(mock_search_data[0])

        assert result == mock_get_data_details


def test_search_kafka_topics_not_found():
    """Verify no results are found based on the query."""
    with patch('external.mcp_tools.search_data', return_value=[]) as search_mock:

        result = search_kafka_topics(query="non_existent")

        search_mock.assert_called_once_with(query="non_existent", search_filter={"type": "kafka_topic"})

        assert result == {}
