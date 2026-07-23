import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_auth_sign_in_happy_path(client: AsyncClient):
    response = await client.post(
        "/auth/sign-in", json={"email": "test@example.com", "password": "securepassword"}
    )
    assert response.status_code == 200
    expected_keys = {"access_token", "refresh_token"}
    data = response.json()
    assert set(expected_keys).issubset(data.keys())

# Additional tests for the /auth/sign-in endpoint should follow. Each test should address a specific scenario,
# such as missing required fields, invalid data types, etc., as per the instructions.