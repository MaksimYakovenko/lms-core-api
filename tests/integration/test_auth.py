import pytest

@pytest.mark.asyncio
async def test_auth_sign_in_happy_path(client):
    payload = {"email": "user@example.com", "password": "securePassword"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 200
    expected_keys = {"access_token", "refresh_token"}
    assert expected_keys.issubset(response.json().keys())

@pytest.mark.asyncio
async def test_auth_sign_in_missing_email(client):
    payload = {"password": "securePassword"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()

@pytest.mark.asyncio
async def test_auth_sign_in_incorrect_email(client):
    payload = {"email": "invalidEmail", "password": "securePassword"}
    response = await client.post("/auth/sign-in", json=payload)
    assert response.status_code == 422
    assert "detail" in response.json()

# More tests for /auth endpoints following provided scenarios would continue here...