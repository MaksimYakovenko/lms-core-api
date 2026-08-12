import pytest
import httpx

@pytest.mark.asyncio
async def test_registration_and_protected_resource_access(client: httpx.AsyncClient):
    """Test the user registration, login, and accessing a protected resource."""

    # Step 1: Get Captcha
    captcha_response = await client.get("/auth/captcha")
    assert captcha_response.status_code == 200
    captcha_data = captcha_response.json()
    captcha_id, captcha_answer = captcha_data["captcha_id"], captcha_data["captcha_answer"]

    # Step 2: Register a new user
    registration_payload = {
        "email": "tester@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "password123",
        "birthday": "1990-01-01",
        "captcha_id": captcha_id,
        "captcha_answer": captcha_answer
    }
    registration_response = await client.post("/auth/sign-up", json=registration_payload)
    assert registration_response.status_code == 200

    # Step 3: Login the registered user
    login_payload = {"email": "tester@example.com", "password": "password123"}
    login_response = await client.post("/auth/sign-in", json=login_payload)
    assert login_response.status_code == 200
    tokens = login_response.json()
    access_token, refresh_token = tokens["access_token"], tokens["refresh_token"]

    # Step 4: Access a protected resource
    headers = {"Authorization": f"Bearer {access_token}"}
    news_response = await client.get("/news", headers=headers)
    assert news_response.status_code == 200
    assert isinstance(news_response.json(), list)