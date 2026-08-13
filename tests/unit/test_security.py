from __future__ import annotations

## Import Statements
import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from src.authentication.security import create_security_middleware

## Define Helper Function
def build_test_app():
    app = FastAPI()
    app.add_middleware(create_security_middleware())

    @app.get("/")
    async def root():
        return {"message": "Hello World!"}

    return app

## Tests
def test_root_authenticated() -> None:
    app = build_test_app()
    client = TestClient(app)
    response = client.get("/", headers={"Authorization": "Bearer VALID_TOKEN"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

def test_root_unauthenticated() -> None:
    app = build_test_app()
    client = TestClient(app)
    response = client.get("/", headers={"Authorization": "Bearer INVALID_TOKEN"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid or expired token."

def test_root_rate_limiting() -> None:
    app = build_test_app()
    client = TestClient(app)
    headers = {"Authorization": "Bearer VALID_TOKEN"}
    # Send successful requests within rate limit
    for _ in range(5):
        response = client.get("/", headers=headers)
        assert response.status_code == 200
    # Test exceeding the limit
    response = client.get("/", headers=headers)
    assert response.status_code == 429
    assert response.json()["detail"] == "Rate limit exceeded."
