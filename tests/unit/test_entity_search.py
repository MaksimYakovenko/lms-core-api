import pytest
from unittest.mock import AsyncMock, patch
from src.data_catalog.entity_search import DataCatalog, query_kafka_topic, build_query

@pytest.mark.asyncio
async def test_query_kafka_topic_returns_result():
    mock_pool = AsyncMock()
    mock_connection = AsyncMock()
    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection

    mock_connection.fetch.return_value = [{'topic_name': 'test_topic'}]

    with patch('src.data_catalog.entity_search.create_pool', return_value=mock_pool):
        result = await query_kafka_topic('test_topic')

    assert result == {'topic_name': 'test_topic'}

@pytest.mark.asyncio
async def test_query_kafka_topic_no_topic():
    with pytest.raises(ValueError, match="Topic name cannot be empty."):
        await query_kafka_topic('')

@pytest.mark.asyncio
async def test_query_kafka_topic_no_results():
    mock_pool = AsyncMock()
    mock_connection = AsyncMock()
    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection

    mock_connection.fetch.return_value = []

    with patch('src.data_catalog.entity_search.create_pool', return_value=mock_pool):
        result = await query_kafka_topic('nonexistent_topic')

    assert result is None

@pytest.mark.asyncio
async def test_datacatalog_initialization():
    mock_pool = AsyncMock()
    with patch('src.data_catalog.entity_search.create_pool', return_value=mock_pool):
        catalog = DataCatalog('mock_db_url')
        await catalog.initialize()
    mock_pool.assert_called_once_with(dsn='mock_db_url')

@pytest.mark.asyncio
async def test_datacatalog_closed():
    mock_pool = AsyncMock()
    with patch('src.data_catalog.entity_search.create_pool', return_value=mock_pool):
        catalog = DataCatalog('mock_db_url')
        await catalog.initialize()
        await catalog.close()
    mock_pool.close.assert_called_once()
