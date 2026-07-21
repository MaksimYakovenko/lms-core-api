import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_auth_and_protected_resource_flow(client: AsyncClient):
    """Test the registration, login, and access to protected resource workflow."""

    # Step 1: User registration
    registration_payload = {
        "email": "testuser@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "SecurePa55!",
        "birthday": "1990-01-01",
        "captcha_id": "dummy",
        "captcha_answer": "42"
    }
    response = await client.post("/auth/sign-up", json=registration_payload)
    assert response.status_code == 200

    # Step 2: User login
    login_payload = {
        "email": registration_payload["email"],
        "password": registration_payload["password"]
    }
    response = await client.post("/auth/sign-in", json=login_payload)
    assert response.status_code == 200
    auth_data = response.json()
    access_token = auth_data["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}

    # Step 3: Access a protected resource
    response = await client.get("/users/me", headers=headers)
    assert response.status_code == 200
    user_data = response.json()
    assert user_data["email"] == registration_payload["email"]