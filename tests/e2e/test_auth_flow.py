import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_and_login(client: AsyncClient):
    """Test the user registration and login flow."""
    # Get captcha for registration
    captcha_response = await client.get("/auth/captcha")
    assert captcha_response.status_code == 200
    captcha_data = captcha_response.json()

    # Register new user
    new_user_data = {
        "email": "test.user@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "Secure1Password",
        "birthday": "1990-01-01",
        "captcha_id": captcha_data["captcha_id"],
        "captcha_answer": "1234"  # Assume for simplicity
    }
    register_response = await client.post("/auth/sign-up", json=new_user_data)
    assert register_response.status_code == 200

    # Log in as the new user
    login_data = {
        "email": "test.user@example.com",
        "password": "Secure1Password",
    }
    login_response = await client.post("/auth/sign-in", json=login_data)
    assert login_response.status_code == 200
    tokens = login_response.json()
    assert "access_token" in tokens