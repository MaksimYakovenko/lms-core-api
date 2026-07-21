import pytest
from unittest.mock import patch, AsyncMock
from src.mcp_source_validation import MCPDataValidator

@pytest.mark.asyncio
async def test_fetch_data_valid_key():
    """Test fetching data with a valid key."""
    db_url = "postgres://user:password@localhost/testdb"
    validator = MCPDataValidator(db_url)

    mock_data = {"key": "test_key", "value": "test_value"}

    with patch("asyncpg.create_pool", new_callable=AsyncMock) as mock_create_pool:
        mock_pool = AsyncMock()
        mock_connection = AsyncMock()
        mock_connection.fetchrow.return_value = mock_data
        mock_pool.acquire.return_value = mock_connection
        mock_create_pool.return_value = mock_pool

        result = await validator.fetch_data("test_key")

    assert result == mock_data

@pytest.mark.asyncio
async def test_fetch_data_invalid_key():
    """Test fetching data with an invalid key."""
    db_url = "postgres://user:password@localhost/testdb"
    validator = MCPDataValidator(db_url)

    with patch("asyncpg.create_pool", new_callable=AsyncMock) as mock_create_pool:
        mock_pool = AsyncMock()
        mock_connection = AsyncMock()
        mock_connection.fetchrow.return_value = None
        mock_pool.acquire.return_value = mock_connection
        mock_create_pool.return_value = mock_pool

        with pytest.raises(ValueError, match="No data found for key: invalid_key"):
            await validator.fetch_data("invalid_key")

@pytest.mark.asyncio
async def test_fetch_data_pool_error():
    """Test pool creation error."""
    db_url = "postgres://user:password@localhost/testdb"
    validator = MCPDataValidator(db_url)

    with patch("asyncpg.create_pool", side_effect=Exception("Pool error")):
        with pytest.raises(Exception, match="Pool error"):
            await validator.fetch_data("test_key")