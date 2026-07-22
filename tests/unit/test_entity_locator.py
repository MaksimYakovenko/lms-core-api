from __future__ import annotations

import asyncio
from src.data_catalog.entity_locator import EntityLocator  # Adjust the import path accordingly

def test_entity_locator() -> None:
    """Tests the EntityLocator locating functionality."""
    async def test_logic() -> None:
        instance = EntityLocator("test_topic")
        result = await instance.locate_entity()
        assert "entity_id" in result and result["entity_id"] == "1234"
    asyncio.run(test_logic())
