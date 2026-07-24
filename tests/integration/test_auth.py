import pytest
import httpx

@pytest.mark.asyncio
async def test_auth_sign_in(client):
    response = await client.post('/auth/sign-in', json={'email': 'user@example.com', 'password': 'securepassword'})
    assert response.status_code == 200
    assert 'access_token' in response.json()
    assert 'refresh_token' in response.json()

@pytest.mark.asyncio
async def test_auth_sign_in_missing_field(client):
    response = await client.post('/auth/sign-in', json={'email': 'user@example.com'})
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_auth_sign_in_wrong_type(client):
    response = await client.post('/auth/sign-in', json={'email': 12345, 'password': True})
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_auth_sign_in_duplicate(client):
    response_1 = await client.post('/auth/sign-in', json={'email': 'user@example.com', 'password': 'securepassword'})
    response_2 = await client.post('/auth/sign-in', json={'email': 'user@example.com', 'password': 'securepassword'})
    assert response_1.status_code == 200
    assert response_2.status_code in [200, 409] # Assuming conflict scenario or repeat is allowed

# Continue with similar tests for `/auth/sign-up`, `/auth/refresh`, and other endpoints.