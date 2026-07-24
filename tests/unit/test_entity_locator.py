import pytest
import os
from unittest.mock import AsyncMock, MagicMock, patch
from src.entity_locator import EntityLocator

@pytest.mark.asyncio
async def test_locate_entity_topic_found():
    """
    Test locate_entity behavior when the topic is found.
    """
    mock_pool = AsyncMock()
    mock_connection = AsyncMock()
    mock_fetchrow = AsyncMock()
    mock_fetchrow.return_value = {
        "attributes": {"key": "value"},
        "governance_information": {"policy": "details"},
        "links": ["link1", "link2"],
    }
    mock_connection.fetchrow = mock_fetchrow

    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection

    with patch("src.entity_locator.asyncpg.create_pool", return_value=mock_pool):
        os.environ["DATABASE_URL"] = "mock_database_url"

        locator = EntityLocator("test-topic")
        result = await locator.locate_entity()

        assert result == {
            "attributes": {"key": "value"},
            "governance_information": {"policy": "details"},
            "links": ["link1", "link2"],
        }

@pytest.mark.asyncio
async def test_locate_entity_topic_not_found():
    """
    Test locate_entity behavior when the topic is not found.
    """
    mock_pool = AsyncMock()
    mock_connection = AsyncMock()
    mock_fetchrow = AsyncMock()
    mock_fetchrow.return_value = None
    mock_connection.fetchrow = mock_fetchrow

    mock_pool.acquire.return_value.__aenter__.return_value = mock_connection

    with patch("src.entity_locator.asyncpg.create_pool", return_value=mock_pool):
        os.environ["DATABASE_URL"] = "mock_database_url"

        locator = EntityLocator("nonexistent-topic")
        result = await locator.locate_entity()

        assert result is None

@pytest.mark.asyncio
async def test_locate_entity_database_url_not_set():
    """
    Test locate_entity raises ValueError when DATABASE_URL is not set.
    """
    os.environ.pop("DATABASE_URL", None)

    locator = EntityLocator("test-topic")

    with pytest.raises(ValueError, match="DATABASE_URL environment variable is not set."):
        await locator.locate_entity()

@pytest.mark.asyncio
async def test_locate_entity_query_error():
    """
    Test locate_entity raises RuntimeError on query failure.
    """
    mock_pool = AsyncMock()

    def side_effect(*args, **kwargs):
        raise asyncpg.PostgresError("mock error")

    mock_pool.acquire.return_value.__aenter__.side_effect = side_effect

    with patch("src.entity_locator.asyncpg.create_pool", return_value=mock_pool):
        os.environ["DATABASE_URL"] = "mock_database_url"

        locator = EntityLocator("test-topic")

        with pytest.raises(RuntimeError, match="Database query failed."):
            await locator.locate_entity()