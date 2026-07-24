import pytest
from unittest.mock import AsyncMock, patch
from src.data_catalog import DataEntityRetriever, fallback_mechanism

@pytest.mark.asyncio
async def test_fetch_entity_success():
    async with patch("aiohttp.ClientSession.get", new_callable=AsyncMock) as mock_get:
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response

        retriever = DataEntityRetriever()
        data = await retriever.fetch_entity(1234)
        await retriever.close()

        assert data == {"key": "value"}
        mock_get.assert_called_once_with(
            "https://datacatalog.epam.com/data/data-details/1234/summary?utm_source=onehub-assistant&utm_medium=widget"
        )

@pytest.mark.asyncio
async def test_fetch_entity_not_found():
    async with patch("aiohttp.ClientSession.get", new_callable=AsyncMock) as mock_get:
        mock_response = AsyncMock()
        mock_response.status = 404
        mock_get.return_value = mock_response

        retriever = DataEntityRetriever()
        data = await retriever.fetch_entity(5678)
        await retriever.close()

        assert data == None


def test_fallback_mechanism():
    result = fallback_mechanism(255703)
    assert result == None