from __future__ import annotations

import asyncio
import pytest
from src.data_catalog.entity_retrieval import create_data_catalog

@pytest.mark.asyncio
async def test_retrieve_entity_details() -> None:
    """Test the retrieve_entity_details method."""
    catalog = create_data_catalog()
    # Mock environment or use a test database
    entity_id = "test-entity"
    result = await catalog.retrieve_entity_details(entity_id)
    assert "entity_id" in result
    assert result["entity_id"] == entity_id
    assert "basic" in result
    assert "governance" in result
    assert "links" in result
