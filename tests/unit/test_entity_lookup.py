import pytest
from unittest import mock
from src.data_catalog.entity_lookup import DataCatalogLookup

# Test suite for the DataCatalogLookup class

def test_search_data_normal():
    """Test that search_data returns the correct structure."""
    kafka_topic = "example_topic"
    lookup = DataCatalogLookup(kafka_topic)
    result = lookup.search_data()
    assert result["filters"] == {"topic": kafka_topic}
    assert "entities" in result
    assert isinstance(result["entities"], list)

def test_get_data_details_normal():
    """Test that get_data_details returns the correct structure."""
    kafka_topic = "example_topic"
    lookup = DataCatalogLookup(kafka_topic)
    entity_id = "sample_entity_id"
    details = lookup.get_data_details(entity_id)
    assert details["entity_id"] == entity_id
    assert "details" in details
    assert isinstance(details["details"], list)