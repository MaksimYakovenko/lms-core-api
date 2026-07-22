import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_registration_login_access_protected_resource():
    # Simulate user registration and login flow
    base_url = "http://localhost:8000"

    async with AsyncClient(base_url=base_url) as client:

        # Obtain a captcha for registration
        captcha_response = await client.get("/auth/captcha")
        assert captcha_response.status_code == 200
        captcha_id = captcha_response.json().get("captcha_id")
        captcha_answer = "example answer"  # Mocked answer

        # Perform user registration
        registration_payload = {
            "email": "user@example.com",
            "first_name": "First",
            "last_name": "Last",
            "password": "securepassword",
            "birthday": "2000-01-01",
            "captcha_id": captcha_id,
            "captcha_answer": captcha_answer,
        }
        registration_response = await client.post("/auth/sign-up", json=registration_payload)
        assert registration_response.status_code == 200
        
        # Log in using the registered credentials
        login_payload = {
            "email": "user@example.com",
            "password": "securepassword",
        }
        login_response = await client.post("/auth/sign-in", json=login_payload)
        assert login_response.status_code == 200

        # Extract access token
        access_token = login_response.json().get("access_token")
        assert access_token is not None

        # Access a protected resource
        protected_headers = {"Authorization": f"Bearer {access_token}"}
        protected_response = await client.get("/users/me", headers=protected_headers)
        assert protected_response.status_code == 200
        
        # Confirm returned user information matches registered details
        user_info = protected_response.json()
        assert user_info.get("email") == "user@example.com"
        assert user_info.get("first_name") == "First"
        assert user_info.get("last_name") == "Last"