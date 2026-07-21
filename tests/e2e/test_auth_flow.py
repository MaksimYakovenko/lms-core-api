import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_register_and_access_protected_resource(auth_headers):
    """
    Test registering a new user and accessing a protected resource with the resulting token.
    """
    # Setup the HTTP client
    async with AsyncClient(base_url="http://localhost:8000") as client:
        # Get a captcha for the registration process
        captcha_response = await client.get("/auth/captcha")
        assert captcha_response.status_code == 200
        captcha_data = captcha_response.json()
        captcha_id = captcha_data.get("id")
        captcha_answer = captcha_data.get("answer")

        # Register a new account using captcha
        register_payload = {
            "email": "test@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "securepassword123",
            "birthday": "1990-01-01",
            "captcha_id": captcha_id,
            "captcha_answer": captcha_answer
        }
        register_response = await client.post("/auth/sign-up", json=register_payload)
        assert register_response.status_code == 200

        # Log in using the newly created account
        login_payload = {
            "email": "test@example.com",
            "password": "securepassword123"
        }
        login_response = await client.post("/auth/sign-in", json=login_payload)
        assert login_response.status_code == 200
        tokens = login_response.json()
        access_token = tokens["access_token"]

        # Access a protected resource using the access token
        headers = {"Authorization": f"Bearer {access_token}"}
        protected_response = await client.get("/users/me", headers=headers)
        assert protected_response.status_code == 200

        # Verify the protected resource response
        user_info = protected_response.json()
        assert user_info["email"] == "test@example.com"