from __future__ import annotations

import pytest
from src.data_catalog.entity_lookup import DataCatalogLookup

def test_search_data_no_results() -> None:
    lookup = DataCatalogLookup(kafka_topic="test-topic")
    results = lookup.search_data()
    assert "entities" in results
    assert isinstance(results["entities"], list)

def test_get_data_details() -> None:
    lookup = DataCatalogLookup(kafka_topic="test-topic")
    details = lookup.get_data_details(entity_id="test_id")
    assert "entity_id" in details
    assert details["entity_id"] == "test_id"
