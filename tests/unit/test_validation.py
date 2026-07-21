from __future__ import annotations

import asyncio
import pytest
from src.data_catalog.validation import DataValidator
from unittest.mock import AsyncMock, MagicMock

@pytest.mark.asyncio
async def test_validate_data_source() -> None:
    """Test the validate_data_source function in DataValidator."""

    mock_pool = MagicMock()
    mock_connection = AsyncMock()
    mock_pool.acquire = AsyncMock(return_value=mock_connection)
    mock_connection.fetchval = AsyncMock(return_value=True)

    validator = DataValidator(db_url="mock://db")
    validator._pool = mock_pool

    result = await validator.validate_data_source(source_id=1)
    assert result is True

    mock_connection.fetchval.assert_called_once_with("SELECT is_mcp_source FROM source_table WHERE id = $1", 1)
