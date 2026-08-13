from __future__ import annotations

import os
import asyncio
import pytest
from httpx import AsyncClient

def test_authentication_workflow() -> None:
    """Test the authentication and profile retrieval workflow."""
    async def perform_test() -> None:
        # Setup
        base_url = os.getenv("SERVICE_URL", "http://127.0.0.1:8000")
        async with AsyncClient(base_url=base_url) as client:
            # Step 1: Register a user
            register_data = {"username": "test_user", "password": "test_pass"}
            register_response = await client.post("/register", json=register_data)
            assert register_response.status_code == 201, register_response.text
            
            # Step 2: Authenticate the user
            auth_data = {"username": "test_user", "password": "test_pass"}
            auth_response = await client.post("/auth", json=auth_data)
            assert auth_response.status_code == 200, auth_response.text
            token = auth_response.json().get("access_token")
            assert token
            
            # Step 3: Retrieve the profile
            headers = {"Authorization": f"Bearer {token}"}
            profile_response = await client.get("/profile", headers=headers)
            assert profile_response.status_code == 200, profile_response.text
            profile_data = profile_response.json()
            assert profile_data.get("username") == "test_user"

    asyncio.run(perform_test())

if __name__ == "__main__":
    pytest.main([__file__])
