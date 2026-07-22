from __future__ import annotations

import pytest
import os
from src.data_catalog.entity_locator import locate_entities

@pytest.mark.asyncio
async def test_locate_entities(monkeypatch):
    """Test the locate_entities function."""
    test_url = "postgresql://demo_user@localhost/demo"
    monkeypatch.setenv("DATABASE_URL", test_url)
    
    filter_conditions = {"name": "example"}
    
    results = await locate_entities(filter_conditions)
    assert isinstance(results, list)
