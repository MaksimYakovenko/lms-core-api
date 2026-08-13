from __future__ import annotations

from fastapi.testclient import TestClient
from src.api.profile_endpoint import app

def test_profile_endpoint_authenticated() -> None:
    """Test that the authenticated profile endpoint returns correct user data."""
    client = TestClient(app)
    response = client.get("/api/profile", headers={"Authorization": "Bearer valid_token_john"})
    assert response.status_code == 200
    assert response.json() == {"name": "John Doe", "email": "john_doe@example.com"}

def test_profile_endpoint_unauthenticated() -> None:
    """Test that unauthenticated access to the profile endpoint returns 401."""
    client = TestClient(app)
    response = client.get("/api/profile")
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized"}

def test_profile_endpoint_nonexistent_user() -> None:
    """Test that access with a valid token for a nonexistent user returns 404."""
    client = TestClient(app)
    response = client.get("/api/profile", headers={"Authorization": "Bearer valid_token_nonexistent"})
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
