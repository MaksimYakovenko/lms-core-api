import pytest

@pytest.mark.asyncio
async def test_user_registration_and_login(client):
    # Step 1: Retrieve captcha for registration
    captcha_response = await client.get("/auth/captcha")
    assert captcha_response.status_code == 200
    captcha = captcha_response.json()

    # Step 2: Register new user
    registration_payload = {
        "email": "testuser@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "securePwd1!",
        "birthday": "2000-01-01",
        "captcha_id": captcha["id"],
        "captcha_answer": "correct_answer"
    }
    registration_response = await client.post("/auth/sign-up", json=registration_payload)
    assert registration_response.status_code == 200

    # Step 3: Log in using registered credentials
    login_payload = {"email": "testuser@example.com", "password": "securePwd1!"}
    login_response = await client.post("/auth/sign-in", json=login_payload)
    assert login_response.status_code == 200
    auth_tokens = login_response.json()

    # Step 4: Access protected resource using obtained token
    auth_headers = {"Authorization": f"Bearer {auth_tokens['access_token']}"}
    user_info_response = await client.get("/users/me", headers=auth_headers)
    assert user_info_response.status_code == 200
    user_info = user_info_response.json()
    assert user_info["email"] == "testuser@example.com"

    # Cleanup step
    # Optionally perform cleanup operations if necessary

# Additional test scenarios can be added below