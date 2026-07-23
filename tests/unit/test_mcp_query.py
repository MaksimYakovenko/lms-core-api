import pytest
from unittest import mock
from asyncpg import Connection
from src.data_catalog_interaction.mcp_query import MCPDataHandler

pytestmark = pytest.mark.asyncio

@mock.patch("src.data_catalog_interaction.mcp_query.create_pool")
async def test_search_data_valid_query(mock_create_pool):
    mock_connection = mock.AsyncMock(spec=Connection)
    mock_connection.fetch.return_value = [{'resource_name': 'example_resource'}]
    mock_pool = mock.AsyncMock()
    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection
    mock_create_pool.return_value.__aenter__.return_value = mock_pool

    os.environ['DATABASE_URL'] = 'mock_database_url'

    handler = MCPDataHandler()
    result = await handler.search_data('example_query')

    assert result == ['example_resource']
    mock_create_pool.assert_called_with('mock_database_url')
    mock_connection.fetch.assert_called_with('SELECT resource_name FROM mcp_data WHERE query = $1', 'example_query')

@mock.patch("src.data_catalog_interaction.mcp_query.create_pool")
async def test_get_data_details_valid_resource(mock_create_pool):
    mock_connection = mock.AsyncMock(spec=Connection)
    mock_connection.fetch.return_value = [{'resource_name': 'example_resource', 'detail': 'example_detail'}]
    mock_pool = mock.AsyncMock()
    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection
    mock_create_pool.return_value.__aenter__.return_value = mock_pool

    os.environ['DATABASE_URL'] = 'mock_database_url'

    handler = MCPDataHandler()
    result = await handler.get_data_details('example_resource')

    assert result == {'resource_name': 'example_resource', 'detail': 'example_detail'}
    mock_create_pool.assert_called_with('mock_database_url')
    mock_connection.fetch.assert_called_with('SELECT * FROM mcp_data WHERE resource_name = $1', 'example_resource')

@mock.patch("src.data_catalog_interaction.mcp_query.create_pool")
async def test_search_data_database_error(mock_create_pool):
    mock_connection = mock.AsyncMock(spec=Connection)
    mock_connection.fetch.side_effect = RuntimeError("Database error")
    mock_pool = mock.AsyncMock()
    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection
    mock_create_pool.return_value.__aenter__.return_value = mock_pool

    os.environ['DATABASE_URL'] = 'mock_database_url'

    handler = MCPDataHandler()
    with pytest.raises(RuntimeError, match="Database error occurred during search_data"):
        await handler.search_data('example_query')