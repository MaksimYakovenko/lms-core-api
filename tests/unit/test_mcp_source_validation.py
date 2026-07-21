from __future__ import annotations

# Unit tests for MCPDataValidator
import pytest
from src.mcp_source_validation import MCPDataValidator

@pytest.mark.asyncio
async def test_mcp_data_validator() -> None:
    """
    Test the MCPDataValidator.validate_data() method.
    """
    # Test variables
    test_url = "postgresql://user:password@localhost/test_db"
    test_key = "test_key"

    validator = MCPDataValidator(db_url=test_url)

    # Mock the asyncpg connection and data reply
    async def mock_fetchrow(query: str, key: str):
        assert query == "SELECT * FROM mcp_data WHERE key = $1"
        if key == test_key:
            return {"key": test_key, "value": "test_value"}
        return None

    asyncpg.create_pool = lambda x: mock_fetchrow

    # Call the method and assert results
    result = await validator.validate_data(test_key)
    assert result == {"key": test_key, "value": "test_value"}

    # Test for missing data
    with pytest.raises(ValueError):
        await validator.validate_data("missing_key")
