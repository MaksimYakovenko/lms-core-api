from __future__ import annotations

import pytest
from src.data_catalog import DataCatalogClient

@pytest.mark.asyncio
class TestDataCatalogClient:
    """Unit tests for DataCatalogClient."""

    async def test_search_data(self) -> None:
        """Test the search_data method."""
        client = DataCatalogClient()
        result = await client.search_data("test-query")
        assert isinstance(result, list)

    async def test_get_data_details(self) -> None:
        """Test the get_data_details method."""
        client = DataCatalogClient()
        result = await client.get_data_details("test-identifier")
        assert isinstance(result, dict)

    async def test_validate_all_mcp(self) -> None:
        """Test the validate_all_mcp method."""
        client = DataCatalogClient()
        await client.validate_all_mcp()
