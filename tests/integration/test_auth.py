import pytest
import httpx

@pytest.mark.asyncio
async def test_auth_sign_in_valid_payload(client):
    response = await client.post("/auth/sign-in", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data

@pytest.mark.asyncio
async def test_auth_sign_in_missing_field(client):
    response = await client.post("/auth/sign-in", json={"email": "test@example.com"})
    assert response.status_code in [400, 422]

@pytest.mark.asyncio
async def test_auth_sign_in_wrong_data_type(client):
    response = await client.post("/auth/sign-in", json={"email": 123, "password": True})
    assert response.status_code in [400, 422]

@pytest.mark.asyncio
async def test_auth_sign_in_invalid_credentials(client):
    response = await client.post("/auth/sign-in", json={"email": "fakeuser@example.com", "password": "wrongpass"})
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_auth_sign_in_unauthorized_request(client):
    response = await client.post("/auth/sign-in")
    assert response.status_code == 401