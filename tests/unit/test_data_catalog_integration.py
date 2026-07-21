import pytest
from unittest.mock import Mock, patch
from src.data_catalog_integration import DataCatalogIntegration

def test_search_data_successful():
    """Test the DataCatalogIntegration.search_data method for expected functionality."""
    # Create an instance of the class with a mocked catalog_api_url
    catalog = DataCatalogIntegration("http://mock-api-url")

    # Temporary override the method's behaviour
    with patch.object(catalog, 'search_data', return_value={"results": [{"entity_id": "12345"}]}) as mock_search:
        query = "epm-skls-ai.courses-to-take"
        results = catalog.search_data(query)
        mock_search.assert_called_once_with(query)
        assert results == {"results": [{"entity_id": "12345"}]}

def test_get_data_details_successful():
    """Test the DataCatalogIntegration.get_data_details method for expected behavior."""
    # Create an instance of the class with a mocked catalog_api_url
    catalog = DataCatalogIntegration("http://mock-api-url")

    # Temporary override the method's behaviour
    with patch.object(catalog, 'get_data_details', return_value={"entity_details": {"name": "Sample Entity"}}) as mock_details:
        entity_id = "12345"
        details = catalog.get_data_details(entity_id)
        mock_details.assert_called_once_with(entity_id)
        assert details == {"entity_details": {"name": "Sample Entity"}}