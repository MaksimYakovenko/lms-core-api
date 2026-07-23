import pytest
import os
from unittest.mock import AsyncMock, MagicMock

# Import the module and functions to test
from src.pipeline.pipeline_execution import execute_pipeline, interact_with_data_catalog_mcp

# Create tests

@pytest.mark.asyncio
async def test_execute_pipeline_runs_successfully():
    """Test that `execute_pipeline` runs successfully."""
    mock_connection = AsyncMock()
    mock_pool = AsyncMock()
    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("asyncpg.create_pool", AsyncMock(return_value=mock_pool))
        mp.setenv("DATABASE_URL", "postgresql://user:pass@localhost/db")

        # Invoke the function
        await execute_pipeline()

        # Ensure internal calls were made as expected
        mock_pool.acquire.assert_called_once()
        mock_connection.fetchrow.assert_called()

@pytest.mark.asyncio
async def test_interact_with_data_catalog_mcp_unsupported_operation():
    """Test that `interact_with_data_catalog_mcp` raises ValueError for unsupported operation."""
    mock_connection = AsyncMock()
    mock_connection.fetchrow.return_value = None

    with pytest.raises(ValueError):
        await interact_with_data_catalog_mcp(
            connection=mock_connection, operation="unsupported_operation", payload={}
        )