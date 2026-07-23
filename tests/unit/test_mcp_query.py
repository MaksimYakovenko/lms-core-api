from __future__ import annotations

import pytest
from unittest.mock import AsyncMock
from src.data_catalog_interaction.mcp_query import MCPDataHandler

@pytest.mark.asyncio
async def test_search_data() -> None:
    handler = MCPDataHandler()
    handler.search_data = AsyncMock(return_value=["topic_1", "topic_2"])

    result = await handler.search_data("query")

    assert result == ["topic_1", "topic_2"]
    handler.search_data.assert_called_once_with("query")

@pytest.mark.asyncio
async def test_get_data_details() -> None:
    handler = MCPDataHandler()
    handler.get_data_details = AsyncMock(return_value={"resource_name": "topic_1", "details": "value"})

    result = await handler.get_data_details("topic_1")

    assert result == {"resource_name": "topic_1", "details": "value"}
    handler.get_data_details.assert_called_once_with("topic_1")
