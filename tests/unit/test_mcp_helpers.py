import pytest
from unittest.mock import AsyncMock
from src.mcp_helpers import get_data_from_mcp, search_data_in_mcp

@pytest.mark.asyncio
async def test_get_data_from_mcp_valid_input():
    """Tests that get_data_from_mcp returns the expected result for a valid input."""
    data_id = "test_id"
    expected_result = {"id": data_id, "name": "Sample Data", "value": 42}
    result = await get_data_from_mcp(data_id)
    assert result == expected_result

@pytest.mark.asyncio
async def test_search_data_in_mcp_valid_input():
    """Tests that search_data_in_mcp returns the expected results for a valid query."""
    query = "test_query"
    expected_result = [
        {"id": "data1", "name": "Sample Data 1"},
        {"id": "data2", "name": "Sample Data 2"}
    ]
    result = await search_data_in_mcp(query)
    assert result == expected_result

@pytest.mark.asyncio
async def test_get_data_from_mcp_async_mocked():
    """Tests get_data_from_mcp with an async mock."""
    mock_data_id = "mock_id"
    mock_result = {"id": mock_data_id, "name": "Mock Data", "value": 99}

    async def mock_get_data_from_mcp(data_id):
        return mock_result

    get_data_from_mcp._original = get_data_from_mcp  # Backup original
    get_data_from_mcp.mock_originals = [get_data_from_mcp._original]
    get_data_from_mcp = AsyncMock(side_effect=mock_get_data_from_mcp)

    result = await get_data_from_mcp(mock_data_id)
    assert result == mock_result

    get_data_from_mcp = get_data_from_mcp._original  # Restore original