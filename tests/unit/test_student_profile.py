import pytest
from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient
from src.endpoints.student_profile import router
from fastapi import FastAPI

# Setup FastAPI app for testing
app = FastAPI()
app.include_router(router)
client = TestClient(app)

@pytest.mark.asyncio
async def test_student_profile_success():
    """Test endpoint with valid JWT and student profile retrieval."""

    valid_jwt = "valid.jwt.token"
    student_id = 123
    mock_profile = {"name": "John Doe", "age": 20}

    with patch("src.endpoints.student_profile.decode_jwt", return_value={"student_id": student_id}):
        with patch("src.endpoints.student_profile.get_student_profile", AsyncMock(return_value=mock_profile)):

            response = client.get(
                "/student/profile",
                headers={"Authorization": f"Bearer {valid_jwt}"},
            )

            assert response.status_code == 200
            assert response.json() == {"profile": mock_profile}

@pytest.mark.asyncio
async def test_student_profile_invalid_jwt():
    """Test endpoint with invalid JWT format."""

    invalid_jwt = "invalid"

    response = client.get(
        "/student/profile",
        headers={"Authorization": f"Bearer {invalid_jwt}"},
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid JWT token."

@pytest.mark.asyncio
async def test_student_profile_missing_auth():
    """Test endpoint with missing Authorization header."""

    response = client.get("/student/profile")

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid or missing JWT token."

@pytest.mark.asyncio
async def test_student_profile_profile_not_found():
    """Test endpoint with student profile not found."""

    valid_jwt = "valid.jwt.token"
    student_id = 123

    with patch("src.endpoints.student_profile.decode_jwt", return_value={"student_id": student_id}):
        with patch("src.endpoints.student_profile.get_student_profile", AsyncMock(side_effect=Exception("Student profile not found."))):

            response = client.get(
                "/student/profile",
                headers={"Authorization": f"Bearer {valid_jwt}"},
            )

            assert response.status_code == 404
            assert response.json()["detail"] == "Student profile not found."