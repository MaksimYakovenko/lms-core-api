import pytest
from unittest.mock import AsyncMock, patch
from asyncpg.pool import Pool
from src.data_catalog.validation import DataValidatorMCP

@pytest.mark.asyncio
async def test_validate_exclusive_use_of_mcp():
    # Test the main validation function
    mock_pool = AsyncMock(spec=Pool)
    mock_connection = AsyncMock()
    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection
    mock_connection.fetchval.return_value = True

    db_url = "postgres://user:password@localhost:5432/database"

    with patch('asyncpg.create_pool', return_value=mock_pool):
        validator = DataValidatorMCP(db_url)
        await validator.setup()

        result = await validator.validate_exclusive_use_of_mcp()

        assert result is True
        
        await validator.teardown()

        mock_connection.fetchval.assert_called_once_with(
            "SELECT EXCLUSIVE_USE_OF_MCP FROM SYSTEM_VALIDATION WHERE SYSTEM_ID = 1"
        )