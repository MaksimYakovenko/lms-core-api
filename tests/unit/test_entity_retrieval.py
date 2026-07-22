from __future__ import annotations

import os
import pytest
from unittest.mock import AsyncMock, patch
from src.entity_retrieval import get_entity

@pytest.mark.asyncio
@patch('src.entity_retrieval.retrieve_entity_data', new_callable=AsyncMock)
async def test_get_entity(mock_retrieve_entity_data: AsyncMock) -> None:
    """
    Test function get_entity to ensure MCP API compliance and data consistency.
    """
    mock_retrieve_entity_data.return_value = {"id": 42, "name": "Entity42"}

    with patch('src.entity_retrieval.POOL'):
        result = await get_entity(42)
        assert result == {"id": 42, "name": "Entity42"}

        mock_retrieve_entity_data.assert_awaited_once_with(42)
