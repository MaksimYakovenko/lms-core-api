import pytest
from unittest.mock import MagicMock
from src.data_connector.catalog import Catalog

def test_catalog_retrieve_topic_metadata_mocks_dependencies():
    catalog = Catalog(mcp_endpoint="http://dummy.endpoint")
    mock_search_data = MagicMock(return_value={"results": [{"entity_ref": "entity_123"}]})
    mock_get_data_details = MagicMock(return_value={
        "entity_ref": "entity_123",
        "details": {"sections": {"basic": {}, "governance": {}, "links": {}}},
    })
    
    catalog.search_data = mock_search_data
    catalog.get_data_details = mock_get_data_details

    topic = "epm-skls-ai.courses-to-take"
    metadata_sections = catalog.retrieve_topic_metadata(topic)

    mock_search_data.assert_called_once_with(topic)
    mock_get_data_details.assert_called_once_with("entity_123")

    assert metadata_sections == {"basic": {}, "governance": {}, "links": {}}