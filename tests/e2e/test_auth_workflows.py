import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_registration_and_access_protected_resource(client: AsyncClient):
    # Verify Captcha retrieval
    captcha_response = await client.get("/auth/captcha")
    assert captcha_response.status_code == 200
    captcha_data = captcha_response.json()

    # Register a new user
    registration_payload = {
        "email": "test_email@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "password": "StrongPass!1",
        "birthday": "2000-01-01",
        "captcha_id": captcha_data["id"],
        "captcha_answer": "42"
    }
    registration_response = await client.post("/auth/sign-up", json=registration_payload)
    assert registration_response.status_code == 200

    # Sign in the user
    login_payload = {
        "email": registration_payload["email"],
        "password": registration_payload["password"]
    }
    login_response = await client.post("/auth/sign-in", json=login_payload)
    assert login_response.status_code == 200
    auth_tokens = login_response.json()

    # Access a protected resource using Bearer Token
    headers = {"Authorization": f"Bearer {auth_tokens['access_token']}"}
    protected_response = await client.get("/news", headers=headers)
    assert protected_response.status_code == 200

    # Test completed