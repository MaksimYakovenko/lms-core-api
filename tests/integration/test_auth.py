import pytest
from httpx import AsyncClient
from pathlib import Path

@pytest.mark.asyncio
async def test_auth_sign_in(client: AsyncClient):
    endpoint = '/auth/sign-in'
    valid_payload = {'email': 'user@example.com', 'password': 'securepassword'}

    # Happy path
    response = await client.post(endpoint, json=valid_payload)
    assert response.status_code == 200
    expected_keys = {'access_token', 'refresh_token'}
    data = response.json()
    assert set(expected_keys).issubset(data.keys())

    # Missing required field
    incomplete_payload = {'email': 'user@example.com'}
    response = await client.post(endpoint, json=incomplete_payload)
    assert response.status_code in {400, 422}

@pytest.mark.asyncio
async def test_auth_sign_up(client: AsyncClient):
    endpoint = '/auth/sign-up'
    valid_payload = {
        'email': 'user@example.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'password': 'securepassword',
        'birthday': '2000-01-01',
        'captcha_id': 'captchaid',
        'captcha_answer': 'captchaanswer'
    }

    # Happy path
    response = await client.post(endpoint, json=valid_payload)
    assert response.status_code == 200
    expected_keys = {'message'}
    data = response.json()
    assert set(expected_keys).issubset(data.keys())

    # Missing required field
    incomplete_payload = {
        'email': 'user@example.com',
        'first_name': 'John',
        'password': 'securepassword',
        'birthday': '2000-01-01',
        'captcha_id': 'captchaid',
        'captcha_answer': 'captchaanswer'
    }
    response = await client.post(endpoint, json=incomplete_payload)
    assert response.status_code in {400, 422}