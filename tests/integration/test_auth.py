import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_auth_sign_in_happy_path(client: AsyncClient):
    response = await client.post('/auth/sign-in', json={'email': 'test@example.com', 'password': 'password123'})
    assert response.status_code == 200
    data = response.json()
    assert set(['access_token', 'refresh_token']).issubset(data.keys())

@pytest.mark.asyncio
async def test_auth_sign_in_missing_email(client: AsyncClient):
    response = await client.post('/auth/sign-in', json={'password': 'password123'})
    assert response.status_code == 422