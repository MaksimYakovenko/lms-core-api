from __future__ import annotations

import pytest
from src.data_connector import Catalog

def test_retrieve_topic_metadata() -> None:
    catalog = Catalog()
    metadata = catalog.retrieve_topic_metadata("epm-skls-ai.courses-to-take")
    assert "basic" in metadata
    assert "governance" in metadata
    assert "links" in metadata
