from __future__ import annotations

import pytest
from unittest.mock import patch, Mock

from src.data_catalog.kafka_topic_search import search_kafka_topics

@patch("src.data_catalog.kafka_topic_search.search_data")
@patch("src.data_catalog.kafka_topic_search.get_data_details")
def test_search_kafka_topics(mock_get_data_details: Mock, mock_search_data: Mock) -> None:
    # Setup mocks
    mock_search_data.return_value = ["mock_topic"]  # Simulate a topic found
    mock_get_data_details.return_value = {"name": "mock_topic", "details": "info"}

    # Call the search function
    query = "example_topic"
    result = search_kafka_topics(query)

    # Asserts
    assert isinstance(result, dict)
    assert result == {"name": "mock_topic", "details": "info"}

    mock_search_data.assert_called_once_with(query=query, search_filter={"type": "kafka_topic"})
    mock_get_data_details.assert_called_once_with("mock_topic")
