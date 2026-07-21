import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_auth_sign_in_happy_path(client: AsyncClient):
    """Test that the /auth/sign-in endpoint works as expected with valid payload."""
    response = await client.post("/auth/sign-in", json={"email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data

# Additional tests for the /auth/sign-in endpoint
# Missing email
@pytest.mark.asyncio
async def test_auth_sign_in_missing_email(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"password": "password"})
    assert response.status_code == 422
# Missing password
@pytest.mark.asyncio
async def test_auth_sign_in_missing_password(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"email": "test@example.com"})
    assert response.status_code == 422
# Invalid email format
@pytest.mark.asyncio
async def test_auth_sign_in_invalid_email_format(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"email": "not-an-email", "password": "password"})
    assert response.status_code == 422
# Non-existent user
@pytest.mark.asyncio
async def test_auth_sign_in_non_existent_user(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"email": "noexist@example.com", "password": "password"})
    assert response.status_code == 401
# Missing Authorization header
@pytest.mark.asyncio
async def test_auth_sign_in_unauthorized(client: AsyncClient):
    response = await client.post("/auth/sign-in")
    assert response.status_code == 422