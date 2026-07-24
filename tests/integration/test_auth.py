import pytest

@pytest.mark.asyncio
async def test_auth_sign_in(client):
    # Happy path: Valid payload
    payload = {"email": "test@example.com", "password": "securepassword"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "refresh_token" in response.json()

@pytest.mark.asyncio
async def test_auth_sign_in_missing_email(client):
    # Missing required field: email
    payload = {"password": "securepassword"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()

@pytest.mark.asyncio
async def test_auth_sign_in_wrong_type_email(client):
    # Wrong data type: email as integer
    payload = {"email": 12345, "password": "securepassword"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()

@pytest.mark.asyncio
async def test_auth_sign_in_non_existent_user(client):
    # Non-existent user scenario
    payload = {"email": "nonexistent@example.com", "password": "fakepassword"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_auth_sign_in_unauthorized(client):
    # Unauthorized request: Invalid Authorization header provided
    payload = {"email": "test@example.com", "password": "securepassword"}
    response = await client.post("/auth/sign-in", json=payload, headers={"Authorization": "invalid"})
    assert response.status_code == 403
