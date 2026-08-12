import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_auth_sign_in(client: AsyncClient):
    url = "http://localhost:8000/auth/sign-in"
    payload = {"email": "test@example.com", "password": "ValidP@ssw0rd"}
    response = await client.post(url, json=payload)
    assert response.status_code == 200
    expected_keys = {"access_token", "refresh_token"}
    assert set(expected_keys).issubset(response.json().keys())


@pytest.mark.asyncio
async def test_auth_sign_in_missing_field(client: AsyncClient):
    url = "http://localhost:8000/auth/sign-in"
    response = await client.post(url, json={"email": "test@example.com"})
    assert response.status_code == 422

...

@pytest.mark.asyncio
async def test_auth_captcha(client: AsyncClient):
    url = "http://localhost:8000/auth/captcha"
    response = await client.get(url)
    assert response.status_code == 200
    assert response.json()  # Verify response structure as needed
