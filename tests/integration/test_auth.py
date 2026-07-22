import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_sign_in(client: AsyncClient):
    response = await client.post(
        '/auth/sign-in', json={'email': 'test@example.com', 'password': 'securepass123'})
    assert response.status_code == 200
    assert all(key in response.json() for key in ['access_token', 'refresh_token'])

# Additional tests for /auth endpoints...

@pytest.mark.asyncio
async def test_sign_up(client: AsyncClient):
    response = await client.post(
        '/auth/sign-up', json={})  # add valid payload here
    assert response.status_code == 200
    assert 'message' in response.json()

# Other endpoints follow similar pattern...