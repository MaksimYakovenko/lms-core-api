import pytest
from unittest.mock import AsyncMock, patch
from src.data_catalog.mcp_transformation import MCPInteractor, DataCatalog

@pytest.mark.asyncio
async def test_fetch_data_success():
    connection_url = "mock://db_url"
    query = "SELECT * FROM test_table"

    with patch("asyncpg.create_pool") as mock_create_pool:
        # Mock the pool and connection
        connection_mock = AsyncMock()
        connection_mock.fetch.return_value = [{"id": 1, "name": "example"}]
        pool_mock = AsyncMock()
        pool_mock.acquire.return_value = connection_mock
        mock_create_pool.return_value.__aenter__.return_value = pool_mock

        mcp_interactor = MCPInteractor(connection_url)
        result = await mcp_interactor.fetch_data(query)

        assert result == [{"id": 1, "name": "example"}]
        connection_mock.fetch.assert_called_once_with(query)

@pytest.mark.asyncio
async def test_fetch_data_failure():
    connection_url = "mock://db_url"
    query = "SELECT * FROM test_table"

    with patch("asyncpg.create_pool") as mock_create_pool:
        # Mock the pool and connection to raise an exception
        pool_mock = AsyncMock()
        pool_mock.acquire.side_effect = Exception("DB Error")
        mock_create_pool.return_value.__aenter__.return_value = pool_mock

        mcp_interactor = MCPInteractor(connection_url)
        result = await mcp_interactor.fetch_data(query)

        assert result == []

@pytest.mark.asyncio
async def test_transform_data_integration():
    connection_url = "mock://db_url"
    query = "SELECT * FROM test_table"

    with patch("asyncpg.create_pool") as mock_create_pool:
        # Mock the pool and connection
        connection_mock = AsyncMock()
        connection_mock.fetch.return_value = [{"id": 1, "name": "example"}]
        pool_mock = AsyncMock()
        pool_mock.acquire.return_value = connection_mock
        mock_create_pool.return_value.__aenter__.return_value = pool_mock

        mcp_interactor = MCPInteractor(connection_url)
        data_catalog = DataCatalog(mcp_interactor)
        result = await data_catalog.transform_data(query)

        assert result == [{"id": 1, "name": "example"}]
        connection_mock.fetch.assert_called_once_with(query)