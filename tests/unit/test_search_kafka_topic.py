import pytest
from unittest.mock import patch, MagicMock
from search_kafka_topic import locate_kafka_topic_details

def test_locate_kafka_topic_details_found():
    """Test that locate_kafka_topic_details returns details if the topic is found."""
    with patch("search_kafka_topic.search_data") as mock_search_data, \
         patch("search_kafka_topic.get_data_details") as mock_get_data_details:
        
        # Mock search_data and get_data_details
        mock_search_data.return_value = [{"id": "123", "name": "example_topic"}]
        mock_get_data_details.return_value = {"details_key": "details_value"}
        
        # Call the function
        topic_details = locate_kafka_topic_details("example_topic")
        
        # Assertions
        assert topic_details == {"details_key": "details_value"}
        mock_search_data.assert_called_once_with({"name": "example_topic"})
        mock_get_data_details.assert_called_once_with("123")

def test_locate_kafka_topic_details_not_found():
    """Test that locate_kafka_topic_details returns None if the topic is not found."""
    with patch("search_kafka_topic.search_data") as mock_search_data:
        
        # Mock search_data
        mock_search_data.return_value = []
        
        # Call the function
        topic_details = locate_kafka_topic_details("example_topic")
        
        # Assertions
        assert topic_details is None
        mock_search_data.assert_called_once_with({"name": "example_topic"})