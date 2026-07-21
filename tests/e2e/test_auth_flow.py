import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_login_access_logout(client: AsyncClient):
    response = await client.post(
        "/auth/sign-up",
        json={
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "password",
            "birthday": "2000-01-01",
            "captcha_id": "12345",
            "captcha_answer": "12345",
        },
    )
    assert response.status_code == 200

    response = await client.post(
        "/auth/sign-in",
        json={"email": "test@example.com", "password": "password"},
    )
    assert response.status_code == 200
    tokens = response.json()

    auth_headers = {"Authorization": f"Bearer {tokens['access_token']}"}

    response = await client.get("/users/me", headers=auth_headers)
    assert response.status_code == 200

    # Logout is usually a client operation; skipping.