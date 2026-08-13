from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from src.authentication.security import SecurityMiddleware

def create_app_with_security_middleware() -> FastAPI:
    app = FastAPI()
    app.add_middleware(SecurityMiddleware)
    @app.get("/")
    async def root():
        return {"message": "Hello, World!"}
    return app

def test_secure_access_valid_token() -> None:
    app = create_app_with_security_middleware()
    client = TestClient(app)
    response = client.get("/", headers={"Authorization": "Bearer VALID_TOKEN"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_secure_access_invalid_token() -> None:
    app = create_app_with_security_middleware()
    client = TestClient(app)
    response = client.get("/", headers={"Authorization": "Bearer INVALID_TOKEN"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid or expired token."

def test_rate_limiting_exceeded() -> None:
    app = create_app_with_security_middleware()
    client = TestClient(app)
    headers = {"Authorization": "Bearer VALID_TOKEN"}
    for _ in range(5):
        response = client.get("/", headers=headers)
        assert response.status_code == 200
    response = client.get("/", headers=headers)
    assert response.status_code == 429
    assert response.json()["detail"] == "Rate limit exceeded."

