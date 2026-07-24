import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_auth_sign_in_happy_path(client: AsyncClient):
    """Test happy path for sign-in endpoint"""
    payload = {"email": "test@example.com", "password": "securepassword123"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 200
    assert {"access_token", "refresh_token"}.issubset(response.json().keys())

@pytest.mark.asyncio
async def test_auth_sign_in_missing_field(client: AsyncClient):
    """Test sign-in endpoint with missing email field"""
    payload = {"password": "securepassword123"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()

# Additional tests for /auth endpoints can be implemented similarly