from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_profile_endpoint_authenticated() -> None:
    headers = {"Authorization": "Bearer dummy-token-valid"}
    response = client.get("/profile", headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_get_profile_endpoint_unauthenticated() -> None:
    response = client.get("/profile")
    assert response.status_code == 401
    assert response.json()["detail"] == "Authentication required"
