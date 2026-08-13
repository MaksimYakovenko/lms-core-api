from __future__ import annotations

from unittest.mock import AsyncMock
from fastapi.testclient import TestClient
from src.endpoints.authenticated_profile import router
from fastapi import FastAPI
import jwt

# Setup test app
app = FastAPI()
app.include_router(router)
client = TestClient(app)

def test_get_profile_valid_token(monkeypatch) -> None:
    """Test profile endpoint with valid JWT."""
    valid_user_id = "1"
    token = jwt.encode({"user_id": valid_user_id}, key="test_secret", algorithm="HS256")

    monkeypatch.setattr("src.endpoints.authenticated_profile.decode_jwt_token", lambda _: {"user_id": valid_user_id})

    async_mock = AsyncMock(return_value={"id": 1, "name": "Test User", "email": "test@example.com"})
    monkeypatch.setattr("src.endpoints.authenticated_profile.retrieve_user_profile", async_mock)

    response = client.get("/profile", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test User", "email": "test@example.com"}

def test_get_profile_invalid_token(monkeypatch) -> None:
    """Test profile endpoint with invalid JWT."""
    invalid_token = "invalid.token.value"

    monkeypatch.setattr("src.endpoints.authenticated_profile.decode_jwt_token", lambda _: (_ for _ in ()).throw(HTTPException(status_code=401)))

    response = client.get("/profile", headers={"Authorization": f"Bearer {invalid_token}"})

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid JWT token"

def test_get_profile_nonexistent_user(monkeypatch) -> None:
    """Test accessing a non-existing user profile."""
    valid_user_id = "1"
    token = jwt.encode({"user_id": valid_user_id}, key="test_secret", algorithm="HS256")

    monkeypatch.setattr("src.endpoints.authenticated_profile.decode_jwt_token", lambda _: {"user_id": valid_user_id})

    async_mock = AsyncMock(return_value=None)
    async_mock.side_effect = HTTPException(status_code=404, detail="User profile not found")
    monkeypatch.setattr("src.endpoints.authenticated_profile.retrieve_user_profile", async_mock)

    response = client.get("/profile", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 404
    assert response.json()["detail"] == "User profile not found"
