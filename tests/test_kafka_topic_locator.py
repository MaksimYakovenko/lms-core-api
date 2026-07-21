"""
Unit tests for `kafka_topic_locator` module.
"""

from __future__ import annotations

import pytest
from docs.kafka_topic_locator import locate_topic

@pytest.mark.asyncio
async def test_locate_topic_found() -> None:
    async def mock_search_data(query: str) -> list[dict[str, str]]:
        return [{"entity_id": "123", "name": "epm-skls-ai.courses-to-take"}]

    async def mock_get_data_details(entity_id: str) -> dict[str, str]:
        return {"entity_id": entity_id, "name": "epm-skls-ai.courses-to-take", "info": "Example details"}

    topic_name = "epm-skls-ai.courses-to-take"
    result = await locate_topic(topic_name, mock_search_data, mock_get_data_details)
    assert result["status"] == "found"
    assert result["details"] is not None

@pytest.mark.asyncio
async def test_locate_topic_not_found() -> None:
    async def mock_search_data(query: str) -> list[dict[str, str]]:
        return []

    async def mock_get_data_details(entity_id: str) -> dict[str, str]:
        return {}

    topic_name = "non-existent-topic"
    result = await locate_topic(topic_name, mock_search_data, mock_get_data_details)
    assert result["status"] == "not_found"
    assert result["details"] is None

@pytest.mark.asyncio
async def test_locate_topic_search_failure() -> None:
    async def mock_search_data(query: str) -> list[dict[str, str]]:
        raise RuntimeError("Search failure")

    async def mock_get_data_details(entity_id: str) -> dict[str, str]:
        return {}

    topic_name = "epm-skls-ai.courses-to-take"
    with pytest.raises(RuntimeError, match="Failed to search the data catalog"):
        await locate_topic(topic_name, mock_search_data, mock_get_data_details)

@pytest.mark.asyncio
async def test_locate_topic_details_failure() -> None:
    async def mock_search_data(query: str) -> list[dict[str, str]]:
        return [{"entity_id": "123", "name": "epm-skls-ai.courses-to-take"}]

    async def mock_get_data_details(entity_id: str) -> dict[str, str]:
        raise RuntimeError("Details failure")

    topic_name = "epm-skls-ai.courses-to-take"
    with pytest.raises(RuntimeError, match="Failed to fetch entity details"):
        await locate_topic(topic_name, mock_search_data, mock_get_data_details)
