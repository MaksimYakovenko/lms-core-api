import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_sign_in_happy_path(client: AsyncClient):
    """Test successful sign in."""
    payload = {"email": "user@example.com", "password": "securepassword"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()