from __future__ import annotations

import asyncio
import pytest
from unittest.mock import AsyncMock, MagicMock
from src.data_catalog.validation import DataValidatorMCP

@pytest.mark.asyncio
async def test_validate_exclusive_use_of_mcp() -> None:
    """
    Test that the validate_exclusive_use_of_mcp method works correctly.
    """

    mock_pool = MagicMock()
    mock_connection = AsyncMock()
    mock_connection.fetchval = AsyncMock(return_value=True)
    mock_pool.acquire = AsyncMock(return_value=mock_connection)

    validator = DataValidatorMCP(db_url="mock://db")
    validator._pool = mock_pool

    result = await validator.validate_exclusive_use_of_mcp()

    assert result is True
    mock_connection.fetchval.assert_called_once_with(
        "SELECT EXCLUSIVE_USE_OF_MCP FROM SYSTEM_VALIDATION WHERE SYSTEM_ID = 1"
    )
