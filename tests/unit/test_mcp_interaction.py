import pytest
import aiohttp
from unittest.mock import AsyncMock, patch, MagicMock
from src.data_catalog.mcp_interaction import MCPInteraction

@pytest.mark.asyncio
async def test_search_data_valid_filters():
    # Test that MCPInteraction.search_data works correctly with valid inputs
    filters = {"type": "Example", "name": "test"}
    expected_result = {"results": [{"id": "1234", "type": "Example"}]}
    async_mock_session = AsyncMock()
    async_mock_session.__aenter__.return_value.post.return_value.json = AsyncMock(return_value=expected_result)

    with patch("aiohttp.ClientSession", return_value=async_mock_session):
        
        mcp_instance = MCPInteraction(base_url="http://mock-url.com")
        result = await mcp_instance.search_data(filters=filters)

        assert result == expected_result

@pytest.mark.asyncio
async def test_get_data_details_valid_id():
    # Test that MCPInteraction.get_data_details works correctly for valid entity_id
    entity_id = "1234"
    expected_result = {"id": "1234", "type": "Example", "details": "Sample Data"}
    async_mock_session = AsyncMock()
    async_mock_session.__aenter__.return_value.get.return_value.json = AsyncMock(return_value=expected_result)

    with patch("aiohttp.ClientSession", return_value=async_mock_session):
        
        mcp_instance = MCPInteraction(base_url="http://mock-url.com")
        result = await mcp_instance.get_data_details(entity_id=entity_id)

        assert result == expected_result