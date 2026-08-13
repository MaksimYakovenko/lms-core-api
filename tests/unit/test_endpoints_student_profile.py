from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from some_jwt_library import encode_jwt
from src.endpoints.student_profile import router

# Mock database service for testing
def mock_get_student_profile(student_id: str) -> dict:
    return {"student_id": student_id, "name": "John Doe"}

# Mock JWT
valid_student_jwt = encode_jwt({"student_id": "12345"})

@pytest.fixture
def client() -> TestClient:
    from fastapi import FastAPI
    app = FastAPI()
    app.include_router(router)
    return TestClient(app)

@pytest.mark.asyncio
async def test_student_profile(client: TestClient) -> None:
    """
    Test the student profile retrieval endpoint.
    """
    response = client.get("/student/profile", headers={"Authorization": f"Bearer {valid_student_jwt}"})

    assert response.status_code == 200
    assert "profile" in response.json()
    assert response.json()["profile"]["name"] == "John Doe"
