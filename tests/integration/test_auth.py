import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_auth_sign_in_happy_path(client: AsyncClient):
    response = await client.post('/auth/sign-in', json={"email":"valid@example.com","password":"password"})
    assert response.status_code == 200
    data = response.json()
    expected_keys = {"access_token", "refresh_token"}
    assert expected_keys.issubset(data.keys())

@pytest.mark.asyncio
async def test_auth_sign_in_missing_field(client: AsyncClient):
    response = await client.post('/auth/sign-in', json={"password":"password"})
    assert response.status_code == 422
    
@pytest.mark.asyncio
async def test_auth_sign_in_invalid_data_type(client: AsyncClient):
    response = await client.post('/auth/sign-in', json={"email":"invalidemail","password":12345})
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_auth_sign_in_unauthorized(client: AsyncClient):
    response = await client.post('/auth/sign-in', json={"email":"nonexistent@example.com","password":"password"})
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_auth_sign_in_duplicate(client: AsyncClient):
    response1 = await client.post('/auth/sign-in', json={"email":"valid@example.com","password":"password"})
    response2 = await client.post('/auth/sign-in', json={"email":"valid@example.com","password":"password"})
    assert response1.status_code == 200
    assert response2.status_code == 200