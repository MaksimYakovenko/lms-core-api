from __future__ import annotations

import pytest
from src.data_catalog_integration import DataCatalogIntegration

@pytest.fixture
def data_catalog_integration() -> DataCatalogIntegration:
    return DataCatalogIntegration("http://mock-api-url")

def test_search_data(data_catalog_integration: DataCatalogIntegration) -> None:
    assert isinstance(data_catalog_integration.search_data("epm-skls-ai.courses-to-take"), dict)

def test_get_data_details(data_catalog_integration: DataCatalogIntegration) -> None:
    assert isinstance(data_catalog_integration.get_data_details("mock_entity_id"), dict)
