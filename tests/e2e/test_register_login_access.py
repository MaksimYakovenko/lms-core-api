import pytest
import httpx
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_user_creation_login_flow(client: AsyncClient):
    """
    Tests the flow of registering a user, logging in, and accessing a protected resource.
    """
    # Step 1: Fetch captcha information
    captcha_response = await client.get("/auth/captcha")
    assert captcha_response.status_code == 200
    captcha_data = captcha_response.json()
    captcha_id = captcha_data.get("captcha_id")
    # Step 2: Register a new user
    registration_data = {
        "email": "test_user@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "securePassword123",
        "birthday": "1990-01-01",
        "captcha_id": captcha_id,
        "captcha_answer": "correct_answer"
    }
    registration_response = await client.post("/auth/sign-up", json=registration_data)
    assert registration_response.status_code == 200
    # Step 3: Log in using the new user's credentials
    login_data = {
        "email": "test_user@example.com",
        "password": "securePassword123"
    }
    login_response = await client.post("/auth/sign-in", json=login_data)
    assert login_response.status_code == 200
    tokens = login_response.json()
    access_token = tokens.get("access_token")
    # Step 4: Access a protected resource using the obtained token
    headers = {"Authorization": f"Bearer {access_token}"}
    protected_response = await client.get("/users/me", headers=headers)
    assert protected_response.status_code == 200
    user_info = protected_response.json()
    assert user_info["email"] == "test_user@example.com"