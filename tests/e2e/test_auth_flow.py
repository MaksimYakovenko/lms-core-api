import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_user_registration_login_and_fetch_protected_resource(client: AsyncClient):
    """
    End-to-end test for user registration, authentication, and accessing a protected resource.
    """

    # Step 1: Obtain a captcha for registration
    response = await client.get("/auth/captcha")
    assert response.status_code == 200
    captcha = response.json()

    # Step 2: Register a new user
    registration_payload = {
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "password": "SecurePassword123",
        "birthday": "2000-01-01",
        "captcha_id": captcha["id"],
        "captcha_answer": captcha["answer"]
    }
    response = await client.post("/auth/sign-up", json=registration_payload)
    assert response.status_code == 200

    # Step 3: Log in with the registered user credentials
    login_payload = {
        "email": "user@example.com",
        "password": "SecurePassword123"
    }
    response = await client.post("/auth/sign-in", json=login_payload)
    assert response.status_code == 200
    tokens = response.json()
    access_token = tokens["access_token"]

    # Step 4: Access a protected resource with the obtained token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = await client.get("/users/me", headers=headers)
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["email"] == "user@example.com"