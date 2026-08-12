from __future__ import annotations

import pytest
from httpx import AsyncClient
from pytest_mock import MockerFixture
from src.data_catalog import DataCatalogClient

@pytest.mark.asyncio
class TestDataCatalogClient:
    """Unit tests for DataCatalogClient."""

    @pytest.fixture
    def mock_httpx_client(self, mocker: MockerFixture):
        """Provides a mocked HTTPX client for dependency injection in the tests."""
        client_mock = mocker.patch("httpx.AsyncClient", autospec=True).return_value
        return client_mock

    async def test_search_data(self, mocker: MockerFixture, mock_httpx_client: AsyncClient) -> None:
        """Test the search_data method by mocking the MCP API response."""

        mock_httpx_client.get.return_value.json.return_value = {
            "results": [{"id": "data1"}, {"id": "data2"}],
        }

        mock_httpx_client.get.return_value.status_code = 200

        mocker.patch("httpx.AsyncClient", return_value=mock_httpx_client)

        client = DataCatalogClient(base_url="https://mock.api/")

        result = await client.search_data("sample-query")

        assert result == ["data1", "data2"]

    async def test_get_data_details(self, mocker: MockerFixture, mock_httpx_client: AsyncClient) -> None:
        """Test the get_data_details method by mocking the MCP API response."""

        mock_httpx_client.get.return_value.json.return_value = {
            "id": "data1",
            "name": "Sample Data",
            "details": "Detailed Info",
        }

        mock_httpx_client.get.return_value.status_code = 200

        mocker.patch("httpx.AsyncClient", return_value=mock_httpx_client)

        client = DataCatalogClient(base_url="https://mock.api/")

        result = await client.get_data_details("data1")

        assert result == {
            "id": "data1",
            "name": "Sample Data",
            "details": "Detailed Info",
        }
