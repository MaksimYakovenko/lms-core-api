from __future__ import annotations

import pytest
from unittest.mock import AsyncMock
from src.data_catalog.entity_details import EntityDetailsFetcher

def test_entity_details_fetcher() -> None:
    """Test the EntityDetailsFetcher for correct data retrieval."""
    mock_client = AsyncMock()
    mock_client.get_data_details.return_value = {
        'basic': {'name': 'EntityName'},
        'governance': {'policy': 'PolicyDetails'},
        'links': {'self': 'http://example.com/entity'}
    }
    fetcher = EntityDetailsFetcher(mock_client)
    entity_id = "test-entity"
    result = fetcher.get_details(entity_id)
    assert result['basic']['name'] == 'EntityName'
    assert result['governance']['policy'] == 'PolicyDetails'
    assert result['links']['self'] == 'http://example.com/entity'
