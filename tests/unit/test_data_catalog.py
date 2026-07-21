from __future__ import annotations

import pytest
from src.data_catalog import DataCatalogClient, validate_all_mcp

class TestDataCatalogClient:
    """Unit tests for DataCatalogClient."""

    def test_search_data(self) -> None:
        """Test the search_data method."""
        client = DataCatalogClient()
        result = client.search_data("test-query")
        assert isinstance(result, list)

    def test_get_data_details(self) -> None:
        """Test the get_data_details method."""
        client = DataCatalogClient()
        result = client.get_data_details("test-identifier")
        assert isinstance(result, dict)


def test_validate_all_mcp() -> None:
    """Test the validate_all_mcp function."""
    validate_all_mcp()
