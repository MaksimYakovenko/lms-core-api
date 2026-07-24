import pytest
import httpx
from typing import Any, List

@pytest.mark.asyncio
async def test_user_auth_flow(client: httpx.AsyncClient) -> None:
    """Test the full user authentication flow, including registration, login, and access of a protected endpoint."""

    # 1. Perform user registration
    get_captcha_response = await client.get("/auth/captcha")
    assert get_captcha_response.status_code == 200
    captcha_id = get_captcha_response.json().get("captcha_id", "")

    reg_payload = {
        "email": "testuser@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "securepass123",
        "birthday": "2000-01-01",
        "captcha_id": captcha_id,
        "captcha_answer": "dummy_answer"
    }
    reg_response = await client.post("/auth/sign-up", json=reg_payload)
    assert reg_response.status_code == 200, reg_response.text

    # 2. Perform user login
    login_payload = {"email": "testuser@example.com", "password": "securepass123"}
    login_response = await client.post("/auth/sign-in", json=login_payload)
    assert login_response.status_code == 200, login_response.text
    tokens = login_response.json()

    # 3. Access a protected endpoint
    headers = {"Authorization": f"Bearer {tokens['access_token']}"}
    user_info_response = await client.get("/users/me", headers=headers)
    assert user_info_response.status_code == 200, user_info_response.text
    user_info = user_info_response.json()
    assert user_info["email"] == "testuser@example.com"