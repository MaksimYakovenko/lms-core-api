# Integration Tests for Auth Resource

import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_auth_sign_in_happy_path(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"email": "user@example.com", "password": "password123"})
    assert response.status_code == 200
    data = response.json()
    assert set(["access_token", "refresh_token"]).issubset(data.keys())

@pytest.mark.asyncio
async def test_auth_sign_in_missing_email(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"password": "password123"})
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data.keys()

@pytest.mark.asyncio
async def test_auth_sign_in_wrong_data_type(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"email": 123, "password": "password123"})
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data.keys()

@pytest.mark.asyncio
async def test_auth_sign_in_nonexistent_user(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"email": "nonexistent@example.com", "password": "password123"})
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_auth_sign_in_unauthorized_request(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"email": "user@example.com", "password": "password123"}, headers={})
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_auth_sign_up_happy_path(client: AsyncClient):
    response = await client.post("/auth/sign-up", json={"email": "newuser@example.com", "first_name": "New", "last_name": "User", "password": "password123", "birthday": "2000-01-01", "captcha_id": "abc123", "captcha_answer": "xyz789"})
    assert response.status_code == 200
    data = response.json()
    assert "message" in data.keys()

# Continue similar test functions for POST /auth/sign-up and other endpoints