from __future__ import annotations

import pytest
from data_catalog.lookup import DataCatalogLookup

def test_entity_lookup() -> None:
    """Test the entity lookup functionality."""
    kafka_topic = "example-topic"
    lookup = DataCatalogLookup(kafka_topic)
    filters = {"key": "value"}
    sections = ["section1", "section2"]
    assert lookup.perform_mcp_entity_lookup(filters, sections) == {}
