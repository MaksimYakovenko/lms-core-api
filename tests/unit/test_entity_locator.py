from __future__ import annotations

# Third-party imports
import pytest
import asyncio
from unittest.mock import AsyncMock, patch

# Project-specific imports
from src.data_catalog.entity_locator import EntityLocator

@pytest.mark.asyncio
async def test_locate_entity_no_result() -> None:
    """Test locating entity when no result is found."""

    entity_locator = EntityLocator(kafka_topic="test_topic")

    async_mock = AsyncMock()
    async_mock.return_value = {}

    with patch("src.data_catalog.epam_interface.search_data", async_mock):
        with pytest.raises(ValueError) as exc_info:
            await entity_locator.locate_entity(async_mock)

    assert str(exc_info.value) == "No entity found for topic: test_topic"

@pytest.mark.asyncio
async def test_locate_entity_success() -> None:
    """Test locating entity with a valid result."""

    entity_locator = EntityLocator(kafka_topic="valid_topic")

    expected_result = {"name": "valid_topic", "details": "Sample details"}
    async_mock = AsyncMock()
    async_mock.return_value = expected_result

    with patch("src.data_catalog.epam_interface.search_data", async_mock):
        result = await entity_locator.locate_entity(async_mock)

    assert result == expected_result
