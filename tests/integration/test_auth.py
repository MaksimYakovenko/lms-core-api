"""
Tests for the Authentication endpoints.
"""

import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_auth_sign_in_happy_path(client: AsyncClient):
    payload = {
        "email": "test@example.com",
        "password": "securePassword"
    }
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 200, "Expected status code 200"
    expected_keys = {"access_token", "refresh_token"}
    data = response.json()
    assert set(expected_keys).issubset(data.keys()), "Response JSON keys mismatch"

@pytest.mark.asyncio
async def test_auth_sign_in_missing_email(client: AsyncClient):
    payload = {
        "password": "securePassword"
    }
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 422, "Expected status code 422"
    data = response.json()
    assert "detail" in data, "Expected 'detail' in response JSON"

# Additional tests for other endpoints and scenarios...
