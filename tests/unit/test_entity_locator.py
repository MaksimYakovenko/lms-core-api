from __future__ import annotations

import pytest
import os
from src.entity_locator import EntityLocator

@pytest.mark.asyncio
async def test_locate_entity_found() -> None:
    """Unit test for the locate_entity method when the topic is found."""
    test_topic = "epm-skls-ai.courses-to-take"
    locator = EntityLocator(test_topic)

    class MockConnection:
        async def fetchrow(self, query: str, topic_name: str) -> dict[str, str | list[str] | None]:
            assert topic_name == test_topic
            return {
                "attributes": {"key": "value"},
                "governance_information": "Info",
                "links": ["https://example.com/kafka-topic-details"],
            }

    class MockPool:
        async def acquire(self):
            return MockConnection()

        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            pass

    asyncpg.create_pool = lambda _: MockPool()

    result = await locator.locate_entity()
    assert result is not None
    assert "attributes" in result
    assert result["attributes"] == {"key": "value"}
    assert result["governance_information"] == "Info"
    assert result["links"] == ["https://example.com/kafka-topic-details"]

@pytest.mark.asyncio
async def test_locate_entity_not_found() -> None:
    """Unit test for the locate_entity method when the topic is not found."""
    test_topic = "nonexistent-topic"
    locator = EntityLocator(test_topic)

    class MockConnection:
        async def fetchrow(self, query: str, topic_name: str) -> None:
            assert topic_name == test_topic
            return None

    class MockPool:
        async def acquire(self):
            return MockConnection()

        async def __aenter__(self):
            return self

        async def __aexit__(self, *args):
            pass

    asyncpg.create_pool = lambda _: MockPool()

    result = await locator.locate_entity()
    assert result is None
