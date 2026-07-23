from __future__ import annotations
import pytest
from src.mcp_helpers import get_data_from_mcp, search_data_in_mcp
import asyncio
@pytest.mark.asyncio
async def test_get_data_from_mcp() -> None:
    data_id = "test_id"
    result = await get_data_from_mcp(data_id)
    assert result == {"id": "test_id", "name": "Sample Data", "value": 42}

@pytest.mark.asyncio
async def test_search_data_in_mcp() -> None:
    query = "sample"
    result = await search_data_in_mcp(query)
    expected_data_ids = {"data1", "data2"}
    assert {entry["id"] for entry in result} == expected_data_ids
