import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_auth_sign_in_happy_path(client: AsyncClient):
    """Test signing in with valid credentials."""
    response = await client.post("http://localhost:8000/auth/sign-in", json={"email": "user@example.com", "password": "password123"})
    assert response.status_code == 200
    data = response.json()
    expected_keys = {"access_token", "refresh_token"}
    assert set(expected_keys).issubset(data.keys())

@pytest.mark.asyncio
async def test_auth_sign_in_missing_email(client: AsyncClient):
    """Test signing in with missing email field."""
    response = await client.post("http://localhost:8000/auth/sign-in", json={"password": "password123"})
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data

@pytest.mark.asyncio
async def test_auth_sign_in_wrong_data_type(client: AsyncClient):
    """Test signing in with wrong data types in payload."""
    response = await client.post("http://localhost:8000/auth/sign-in", json={"email": 123, "password": 456})
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data

@pytest.mark.asyncio
async def test_auth_sign_in_non_existent_resource(client: AsyncClient):
    """Test signing in with non-existent resource."""
    response = await client.post("http://localhost:8000/auth/sign-in", json={"email": "nonexistent@example.com", "password": "wrongpassword"})
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_auth_sign_in_unauthorized_request(client: AsyncClient):
    """Test signing in without authorization header."""
    response = await client.post("http://localhost:8000/auth/sign-in")
    assert response.status_code == 401