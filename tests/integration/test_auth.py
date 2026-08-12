import pytest
from httpx import AsyncClient
@pytest.mark.asyncio
async def test_sign_in_happy_path(client: AsyncClient):
    payload = {"email": "test@example.com", "password": "password123"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 200
    response_data = response.json()
    expected_keys = {"access_token", "refresh_token"}
    assert expected_keys.issubset(response_data.keys())
@pytest.mark.asyncio
async def test_sign_in_missing_email(client: AsyncClient):
    payload = {"password": "password123"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 422