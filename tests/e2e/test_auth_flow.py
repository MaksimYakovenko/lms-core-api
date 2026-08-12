import pytest

@pytest.mark.asyncio
async def test_user_register_and_login_flow(client):
    # Test user registration -> login -> access protected resource.
    captcha_response = await client.get("http://localhost:8000/auth/captcha")
    captcha_id = captcha_response.json().get("captcha_id")
    test_captcha_answer = "captcha"  # Assumption

    registration_data = {
        "email": "testuser@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "securePassword",
        "birthday": "1990-01-01",
        "captcha_id": captcha_id,
        "captcha_answer": test_captcha_answer
    }
    register_response = await client.post("http://localhost:8000/auth/sign-up", json=registration_data)
    assert register_response.status_code == 200

    login_data = {"email": "testuser@example.com", "password": "securePassword"}
    login_response = await client.post("http://localhost:8000/auth/sign-in", json=login_data)
    assert login_response.status_code == 200
    access_token = login_response.json().get("access_token")

    protected_headers = {"Authorization": f"Bearer {access_token}"}
    user_info_response = await client.get("http://localhost:8000/users/me", headers=protected_headers)
    assert user_info_response.status_code == 200