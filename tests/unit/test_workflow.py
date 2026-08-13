from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from src.workflow.main import router

client = TestClient(router)

def test_profile_endpoint() -> None:
    student_id = 123  # Test id
    response = client.get(f"/student/{student_id}/profile")
    assert response.status_code == 200
    assert "profile_detail_key" in response.json()
