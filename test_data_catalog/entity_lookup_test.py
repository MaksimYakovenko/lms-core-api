from __future__ import annotations

import pytest
from unittest.mock import AsyncMock
from data_catalog.entity_lookup import perform_entity_lookup

@pytest.mark.asyncio
async def test_perform_entity_lookup() -> None:
    """Test the perform_entity_lookup function."""
    # Mock the dependencies
    mock_search_data = AsyncMock(return_value=[{"id": "entity-123"}])
    mock_get_data_details = AsyncMock(return_value={"metadata": {}, "schema": {}})

    # Patch the libraries
    search_library.search_data = mock_search_data
    detail_library.get_data_details = mock_get_data_details

    # Call the function
    topic_name = "epm-skls-ai.courses-to-take"
    details = await perform_entity_lookup(topic_name)

    # Validate the result
    assert "metadata" in details
    assert "schema" in details
    mock_search_data.assert_called_once()
    mock_get_data_details.assert_called_once()
