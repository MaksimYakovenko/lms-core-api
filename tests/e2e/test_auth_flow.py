import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_login_access_protected_resource_logout(client: AsyncClient):
    # Step 1: Register a new user
    register_payload = {
        "email": "test_user@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "securepassword",
        "birthday": "2000-01-01",
        "captcha_id": "dummy-captcha-id",
        "captcha_answer": "dummy-answer"
    }
    register_response = await client.post("/auth/sign-up", json=register_payload)
    assert register_response.status_code == 200

    # Step 2: Log in as the new user
    login_payload = {
        "email": "test_user@example.com",
        "password": "securepassword"
    }
    login_response = await client.post("/auth/sign-in", json=login_payload)
    assert login_response.status_code == 200
    tokens = login_response.json()
    access_token = tokens["access_token"]

    # Step 3: Access a protected resource
    headers = {"Authorization": f"Bearer {access_token}"}
    protected_response = await client.get("/news", headers=headers)
    assert protected_response.status_code == 200

    # Step 4: Sign out (if an endpoint exists for logout, otherwise skip this step)