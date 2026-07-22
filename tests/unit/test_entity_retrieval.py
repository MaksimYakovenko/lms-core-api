from __future__ import annotations

import os
import pytest
from unittest.mock import AsyncMock, patch
from src.data_catalog.entity_retrieval import fetch_data_entity

@pytest.mark.asyncio
@patch("src.data_catalog.entity_retrieval.httpx.AsyncClient", autospec=True)
async def test_fetch_data_entity(mock_client: AsyncMock) -> None:
    """
    Test function fetch_data_entity to ensure MCP API compliance and data consistency.
    """
    mock_response = AsyncMock()
    mock_response.json.return_value = {
        "basic": {
            "name": "Test Entity",
            "id": 42
        },
        "governance": {
            "compliance_status": "compliant"
        },
        "links": {
            "homepage": "http://example.com"
        }
    }
    mock_response.raise_for_status.return_value = None
    mock_client.return_value.__aenter__.return_value.get.return_value = mock_response

    with patch("os.getenv", return_value="http://mockapi.example.com"):
        result = await fetch_data_entity("epm-skls-ai.courses-to-take")

    assert result == {
        "basic": {
            "name": "Test Entity",
            "id": 42
        },
        "governance": {
            "compliance_status": "compliant"
        },
        "links": {
            "homepage": "http://example.com"
        }
    }
