import pytest
import httpx
from unittest.mock import AsyncMock, MagicMock
from src.data_catalog import DataCatalogClient

@pytest.mark.asyncio
async def test_DataCatalogClient_request_mcp_success():
    """Test request_mcp method for successful API call."""
    client = DataCatalogClient(base_url="http://api.test")
    mock_response = AsyncMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"key":"value"}

    with pytest.MonkeyPatch.context() as mp:
        mp.setenv("MCP_API_KEY", "test_key")
        mp.setattr(httpx.AsyncClient, "get", AsyncMock(return_value=mock_response))
        result = await client.request_mcp("endpoint", {"param": "value"})

    assert result == {"key": "value"}

@pytest.mark.asyncio
async def test_DataCatalogClient_request_mcp_failure():
    """Test request_mcp method when API returns an error."""
    client = DataCatalogClient(base_url="http://api.test")
    mock_response = AsyncMock()
    mock_response.status_code = 400
    mock_response.text = "error"

    with pytest.MonkeyPatch.context() as mp:
        mp.setenv("MCP_API_KEY", "test_key")
        mp.setattr(httpx.AsyncClient, "get", AsyncMock(return_value=mock_response))
        with pytest.raises(httpx.HTTPError):
            await client.request_mcp("endpoint", {"param": "value"})

@pytest.mark.asyncio
async def test_DataCatalogClient_search_data():
    """Test search_data method for expected outcome."""
    client = DataCatalogClient(base_url="http://api.test")
    mock_request_mcp = AsyncMock(return_value={"results": [{"id": "123"}]} )

    client.request_mcp = mock_request_mcp

    result = await client.search_data("query")

    assert result == ["123"]
