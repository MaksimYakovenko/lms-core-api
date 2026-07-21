import pytest
from unittest.mock import patch
from src.data_catalog_integration import DataCatalogIntegration, catalog_integration

def test_integration_end_to_end():
    """Test DataCatalogIntegration behavior end-to-end."""
    with patch.object(catalog_integration, 'search_data', return_value={"results": [{"entity_id": "12345"}]}) as mock_search,
         patch.object(catalog_integration, 'get_data_details', return_value={"entity_details": {"name": "Sample Entity"}}) as mock_details:
        query = "epm-skls-ai.courses-to-take"
        search_results = catalog_integration.search_data(query)
        mock_search.assert_called_once_with(query)
        assert search_results == {"results": [{"entity_id": "12345"}]}
        
        if search_results["results"]:
            entity_id = search_results["results"][0]["entity_id"]
            entity_details = catalog_integration.get_data_details(entity_id)
            mock_details.assert_called_once_with(entity_id)
            assert entity_details == {"entity_details": {"name": "Sample Entity"}}