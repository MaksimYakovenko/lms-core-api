import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_auth_sign_in_happy_path(client: AsyncClient):
    response = await client.post("/auth/sign-in", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 200
    response_json = response.json()
    expected_keys = {"access_token", "refresh_token"}
    assert expected_keys.issubset(response_json.keys())

# Additional tests would be defined similarly, including edge cases and error validations.