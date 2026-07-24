from __future__ import annotations

import pytest
from src.app.data_retrieval import retrieve_entities

def test_retrieve_entities() -> None:
    """Test the retrieve_entities function."""
    query = "test_query"
    result = retrieve_entities(query)
    assert isinstance(result, list)
    assert all("id" in entity and "name" in entity for entity in result)
