import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_user_registration_and_login_flow(client: AsyncClient):
    # Fetch CAPTCHA
    captcha_response = await client.get("/auth/captcha")
    assert captcha_response.status_code == 200
    captcha_details = captcha_response.json()

    # Register a new user
    registration_payload = {
        "email": "test.user@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "password123",
        "birthday": "1990-01-01",
        "captcha_id": captcha_details["id"],
        "captcha_answer": "42"
    }
    registration_response = await client.post(
        "/auth/sign-up", json=registration_payload
    )
    assert registration_response.status_code == 200

    # Sign in with the new user
    login_payload = {
        "email": "test.user@example.com",
        "password": "password123"
    }
    login_response = await client.post(
        "/auth/sign-in", json=login_payload
    )
    assert login_response.status_code == 200
    tokens = login_response.json()
    
    # Validate the received access token
    auth_headers = {"Authorization": f"Bearer {tokens['access_token']}"}
    user_info_response = await client.get(
        "/users/me", headers=auth_headers
    )
    assert user_info_response.status_code == 200
    user_info = user_info_response.json()
    assert user_info["email"] == "test.user@example.com"