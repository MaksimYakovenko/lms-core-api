import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_registration_login_view_profile(client: AsyncClient):
    """Test user registration, login, and viewing the profile."""
    # Step 1: Retrieve captcha for registration
    captcha_response = await client.get("/auth/captcha")
    assert captcha_response.status_code == 200
    captcha = captcha_response.json()

    # Step 2: Register a new user
    registration_data = {
        "email": "testuser@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "TestPass123",
        "birthday": "2000-01-01",
        "captcha_id": captcha["id"],
        "captcha_answer": captcha["answer"]
    }
    reg_response = await client.post("/auth/sign-up", json=registration_data)
    assert reg_response.status_code == 200
    registration_result = reg_response.json()
    
    # Step 3: Login with the new user credentials
    login_data = {"email": "testuser@example.com", "password": "TestPass123"}
    login_response = await client.post("/auth/sign-in", json=login_data)
    assert login_response.status_code == 200
    tokens = login_response.json()
    
    # Step 4: Use the token to access the protected endpoint
    auth_headers = {"Authorization": f"Bearer {tokens['access_token']}"}
    profile_response = await client.get("/users/me", headers=auth_headers)
    assert profile_response.status_code == 200
    profile_info = profile_response.json()

    # Validate profile information
    assert profile_info["email"] == "testuser@example.com"