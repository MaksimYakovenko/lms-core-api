import pytest
from unittest.mock import patch, AsyncMock
from src.data_catalog.entity_locator import locate_entities
import os

@pytest.mark.asyncio
async def test_locate_entities_environment_variable_unset():
    """Test that the function raises an error if DATABASE_URL is unset."""
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(EnvironmentError, match="DATABASE_URL environment variable not set."):
            await locate_entities({})

@pytest.mark.asyncio
async def test_locate_entities_query_execution():
    """Test that the function constructs and executes the query correctly."""
    mock_db_url = "postgres://user:pass@localhost:5432/db"
    mock_entities = [{"id": 1, "name": "entity1"}, {"id": 2, "name": "entity2"}]

    with patch.dict(os.environ, {"DATABASE_URL": mock_db_url}):
        pool_mock = AsyncMock()
        conn_mock = AsyncMock()
        pool_mock.acquire.return_value.__aenter__.return_value = conn_mock
        conn_mock.fetch.return_value = [mock_entities]

        with patch("asyncpg.create_pool", return_value=pool_mock):
            filter_conditions = {"key": "value"}
            results = await locate_entities(filter_conditions)

            expected_query = "SELECT * FROM entities WHERE key = $1"
            conn_mock.fetch.assert_called_once_with(expected_query, "value")

            assert results == [mock_entities]