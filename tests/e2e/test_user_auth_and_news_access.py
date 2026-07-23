import pytest
from httpx import AsyncClient
from pytest_lazyfixture import lazy_fixture

@pytest.mark.asyncio
async def test_user_auth_and_news_access(client: AsyncClient):
    # Step 1: Sign up a new user
    captcha_response = await client.get("/auth/captcha")
    assert captcha_response.status_code == 200
    captcha_data = captcha_response.json()

    sign_up_data = {
        "email": "test_user@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "SecurePass123",
        "birthday": "1990-01-01",
        "captcha_id": captcha_data["captcha_id"],
        "captcha_answer": "correct_answer",
    }
    sign_up_response = await client.post("/auth/sign-up", json=sign_up_data)
    assert sign_up_response.status_code == 200

    # Step 2: Sign in with the new account
    sign_in_data = {
        "email": "test_user@example.com",
        "password": "SecurePass123",
    }
    sign_in_response = await client.post("/auth/sign-in", json=sign_in_data)
    assert sign_in_response.status_code == 200
    tokens = sign_in_response.json()

    # Step 3: Access news endpoint with the obtained authorization tokens
    headers = {"Authorization": f"Bearer {tokens['access_token']}"}
    news_response = await client.get("/news", headers=headers)
    assert news_response.status_code == 200
    news_data = news_response.json()

    # Final step: Assert fetched news list is valid
    assert isinstance(news_data, list)