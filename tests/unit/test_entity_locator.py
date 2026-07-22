from __future__ import annotations

import pytest
import os
from src.entity_locator import EntityLocator

@pytest.mark.asyncio
async def test_locate_entity() -> None:
    """Unit test for the locate_entity method."""
    test_topic = "epm-skls-ai.courses-to-take"
    locator = EntityLocator(test_topic)

    class MockConnection:
        async def fetchrow(self, query: str, topic_name: str) -> dict[str, str | list[str] | None]:
            assert topic_name == test_topic
            return {
                "attributes": {},
                "governance_information": None,
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
    assert "attributes" in result
    assert "governance_information" in result
    assert "links" in result
