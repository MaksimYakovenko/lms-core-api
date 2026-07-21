from __future__ import annotations

# Unit tests for MCPDataValidator
import pytest
import asyncpg
from unittest.mock import AsyncMock
from src.mcp_source_validation import MCPDataValidator

@pytest.mark.asyncio
async def test_mcp_data_validator() -> None:
    """
    Test the MCPDataValidator.validate_data() method.
    """
    # Test variables
    test_url = "postgresql://user:password@localhost/test_db"
    test_key = "test_key"
    test_data = {"key": test_key, "value": "test_value"}

    validator = MCPDataValidator(db_url=test_url)

    # Mock asyncpg
    mock_pool = AsyncMock()
    mock_connection = AsyncMock()

    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection
    mock_connection.fetchrow = AsyncMock(side_effect=lambda query, key: test_data if key == test_key else None)

    asyncpg.create_pool = AsyncMock(return_value=mock_pool)

    # Call the method and assert results
    result = await validator.fetch_data(test_key)
    assert result == test_data

    # Test for missing data
    with pytest.raises(ValueError):
        await validator.fetch_data("missing_key")
