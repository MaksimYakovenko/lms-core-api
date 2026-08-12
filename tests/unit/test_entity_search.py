import pytest
from unittest.mock import patch, MagicMock
from src.data_catalog.entity_search import locate_entity, DataCatalogService

def test_locate_entity_found():
    """Test case for a found entity."""
    with patch.object(DataCatalogService, 'search_data', return_value=[{"id": "entity-123"},]) as mock_search:
        with patch.object(DataCatalogService, 'get_data_details', return_value={"id": "entity-123", "details": "Sample entity details"}) as mock_get_details:
            result = locate_entity("test-topic")
            assert result == {"id": "entity-123", "details": "Sample entity details"}
            mock_search.assert_called_once_with("entity", {"kafka_topic": "test-topic"})
            mock_get_details.assert_called_once_with("entity-123")

def test_locate_entity_not_found():
    """Test case for an entity not found."""
    with patch.object(DataCatalogService, 'search_data', return_value=[]) as mock_search:
        result = locate_entity("test-topic")
        assert result == {"error": "Entity not found"}
        mock_search.assert_called_once_with("entity", {"kafka_topic": "test-topic"})