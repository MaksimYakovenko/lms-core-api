from __future__ import annotations

import pytest
from data_catalog.entity_lookup import DataCatalogLookup

def test_fetch_entity_details() -> None:
    """Test the fetching of data entity details."""
    lookup = DataCatalogLookup(topic_name="test-topic")
    details = lookup.fetch_entity_details()
    assert details["id"] == "entity123"
    assert "schema" in details["details"]
