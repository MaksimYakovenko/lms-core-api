import pytest
from unittest.mock import AsyncMock
from src.data_catalog.entity_locator import EntityLocator
import asyncio

@pytest.mark.asyncio
async def test_locate_entity_success():
    # Test successful retrieval
    mock_search_data = AsyncMock(return_value={"entity_id": 123, "name": "Test Entity"})
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("src.data_catalog.entity_locator.search_data", mock_search_data)
        locator = EntityLocator(kafka_topic="test_topic")
        result = await locator.locate_entity(None)  # Pass None for db_pool due to its non-utilization
        assert result == {"entity_id": 123, "name": "Test Entity"}
        mock_search_data.assert_called_once_with({"topic": "test_topic"})

@pytest.mark.asyncio
async def test_locate_entity_not_found():
    # Test no entity found scenario
    mock_search_data = AsyncMock(return_value=None)
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("src.data_catalog.entity_locator.search_data", mock_search_data)
        locator = EntityLocator(kafka_topic="test_topic")
        with pytest.raises(ValueError, match="No entity found for topic: test_topic"):
            await locator.locate_entity(None)  # Pass None for db_pool due to its non-utilization
