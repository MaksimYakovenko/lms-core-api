"""
This module contains end-to-end tests for authentication workflows.
"""

import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_login_access_protected_resource(client: AsyncClient):
    """
    Test the user registration and authentication flow.
    Scenarios:
    1. Register a new user.
    2. Login with the registered credentials.
    3. Access a protected endpoint using the obtained token.
    """

    # Step 1: Register a new user.
    response = await client.post(
        "auth/sign-up",
        json={
            "email": "test_user@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "password2023",
            "birthday": "1990-01-01",
            "captcha_id": "dummy_captcha",
            "captcha_answer": "dummy_answer"
        }
    )
    assert response.status_code == 200

    # Step 2: Log in with the provided credentials.
    response = await client.post(
        "auth/sign-in",
        json={"email": "test_user@example.com", "password": "password2023"}
    )
    assert response.status_code == 200
    tokens = response.json()
    assert "access_token" in tokens
    assert "refresh_token" in tokens

    # Step 3: Access a protected resource.
    auth_headers = {"Authorization": f"Bearer {tokens['access_token']}"}
    response = await client.get("news", headers=auth_headers)
    assert response.status_code == 200