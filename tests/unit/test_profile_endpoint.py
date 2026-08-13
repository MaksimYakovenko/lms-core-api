from __future__ import annotations

import os
from unittest.mock import AsyncMock, patch
import pytest
from starlette.testclient import TestClient
from src.backend_module.profile_endpoint import app

@patch("src.backend_module.profile_endpoint.pool")
@pytest.mark.asyncio
async def test_get_profile(pool_mock: AsyncMock) -> None:
    client = TestClient(app)

    pool_mock.acquire.return_value.__aenter__.return_value.fetchrow = AsyncMock(
        return_value={"id": "1", "name": "John Doe"}
    )

    response = client.get("/profile/1")

    assert response.status_code == 200
    assert response.json() == {"id": "1", "name": "John Doe"}
