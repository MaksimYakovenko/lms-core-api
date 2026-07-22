import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_login_access_resource_flow(client: AsyncClient):
    # STEP 1: Obtain a CAPTCHA
    captcha_response = await client.get("/auth/captcha")
    assert captcha_response.status_code == 200
    captcha_id = captcha_response.json()["id"]
    captcha_answer = "dummy_answer"  # Replace with a valid answer if needed
    
    # STEP 2: Register a new user using the CAPTCHA
    registration_data = {
        "email": "user@example.com",
        "first_name": "First",
        "last_name": "Last",
        "password": "TestPass123",
        "birthday": "2000-01-01",
        "captcha_id": captcha_id,
        "captcha_answer": captcha_answer
    }
    register_response = await client.post("/auth/sign-up", json=registration_data)
    assert register_response.status_code == 200
    assert register_response.json()["message"] == "Registration successful"
    
    # STEP 3: Login using the registered user credentials
    login_data = {
        "email": "user@example.com",
        "password": "TestPass123"
    }
    login_response = await client.post("/auth/sign-in", json=login_data)
    assert login_response.status_code == 200
    tokens = login_response.json()
    access_token = tokens["access_token"]
    
    # STEP 4: Access a protected resource, e.g., fetching user info
    headers = {"Authorization": f"Bearer {access_token}"}
    user_response = await client.get("/users/me", headers=headers)
    assert user_response.status_code == 200
    user_info = user_response.json()
    assert user_info["email"] == "user@example.com"