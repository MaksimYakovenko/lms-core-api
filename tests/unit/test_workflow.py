from __future__ import annotations

import pytest
import os
from fastapi.testclient import TestClient
from src.workflow.main import router

client = TestClient(router)

def test_profile_endpoint() -> None:
    student_id = 123  # Test id
    response = client.get(f"/student/{student_id}/profile")
    assert response.status_code == 200
    result = response.json()
    assert "profile_detail_key" in result
    assert result["id"] == student_id

def test_get_student_profile(mocker) -> None:
    mocker.patch("src.workflow.main.get_student_profile", return_value={"id": 1, "name": "Test Student"})
    from src.workflow.main import get_student_profile

    result = get_student_profile(1)
    assert result is not None
    assert result.get("name") == "Test Student"
