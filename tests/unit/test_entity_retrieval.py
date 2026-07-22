import pytest
import os
from unittest.mock import patch, AsyncMock
from httpx import Response
from src.data_catalog.entity_retrieval import fetch_data_entity

@pytest.mark.asyncio
@patch("httpx.AsyncClient.get", new_callable=AsyncMock)
@patch("os.getenv")
async def test_fetch_data_entity_success(mock_getenv, mock_async_get):
    """Test the success case of fetch_data_entity."""
    # Mock environment variable
    mock_getenv.return_value = "http://mock-api-url"
    # Mock HTTP response
    mock_data = {"basic": {"key": "value"}, "governance": {}, "links": []}
    mock_async_get.return_value = Response(200, json=mock_data)
    # Perform test
    topic = "test-topic"
    result = await fetch_data_entity(topic)
    assert result == {"basic": {"key": "value"}, "governance": {}, "links": []}
    mock_getenv.assert_called_once_with("DATA_CATALOG_API_URL")
    mock_async_get.assert_awaited_once_with(
        f"http://mock-api-url/entities", params={"topic": topic}
    )

@pytest.mark.asyncio
@patch("os.getenv")
async def test_fetch_data_entity_missing_env(mock_getenv):
    """Test the missing environment variable scenario."""
    # Mock environment variable as None
    mock_getenv.return_value = None
    # Perform test
    with pytest.raises(ValueError, match="The environment variable 'DATA_CATALOG_API_URL' is not set."):
        await fetch_data_entity("test-topic")
    mock_getenv.assert_called_once_with("DATA_CATALOG_API_URL")

@pytest.mark.asyncio
@patch("httpx.AsyncClient.get", new_callable=AsyncMock)
@patch("os.getenv")
async def test_fetch_data_entity_api_error(mock_getenv, mock_async_get):
    """Test the API error scenario."""
    # Mock environment variable
    mock_getenv.return_value = "http://mock-api-url"
    # Mock HTTP error
    mock_async_get.side_effect = Exception("API error")
    # Perform test
    with pytest.raises(RuntimeError, match="Failed to retrieve data entity: API error"):
        await fetch_data_entity("test-topic")
    mock_getenv.assert_called_once_with("DATA_CATALOG_API_URL")
    mock_async_get.assert_awaited_once_with(
        f"http://mock-api-url/entities", params={"topic": "test-topic"}
    )