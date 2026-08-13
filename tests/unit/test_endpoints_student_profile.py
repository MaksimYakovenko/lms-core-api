from __future__ import annotations

import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from some_jwt_library import encode_jwt
def mock_get_student_profile(student_id: str) -> dict:
    return {"student_id": student_id, "name": "Test Student"}
from src.endpoints.student_profile import router

@pytest.fixture
def client() -> TestClient:
    from fastapi import FastAPI
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)

@patch("src.endpoints.student_profile.get_student_profile", side_effect=mock_get_student_profile)
def test_student_profile(mocked_get_student_profile, client: TestClient) -> None:
    token = encode_jwt({"student_id": "mock_student_id"})

    response = client.get(
        "/student/profile", headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json() == {"profile": {"student_id": "mock_student_id", "name": "Test Student"}}
