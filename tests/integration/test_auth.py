import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_sign_in_valid(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"email": "user@example.com", "password": "securePassword123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data

@pytest.mark.asyncio
async def test_sign_in_missing_email(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"password": "securePassword123"})
    assert response.status_code == 422