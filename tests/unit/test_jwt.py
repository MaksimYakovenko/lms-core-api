from __future__ import annotations

import pytest
import jwt
from datetime import datetime, timedelta
from src.authentication.jwt import JWTHandler

def generate_test_token(secret: str, sub: str, expire_in: int) -> str:
    payload = {
        "sub": sub,
        "exp": datetime.now() + timedelta(seconds=expire_in),
    }
    return jwt.encode(payload, secret, algorithm="HS256")

def test_validate_token() -> None:
    """Tests the validate_token method of JWTHandler."""
    handler = JWTHandler("testsecret")
    valid_token = generate_test_token("testsecret", "user123", 3600)
    assert handler.validate_token(valid_token) is True

    invalid_token = valid_token + "a"
    assert handler.validate_token(invalid_token) is False

    expired_token = generate_test_token("testsecret", "user123", -10)
    assert handler.validate_token(expired_token) is False

def test_get_identity() -> None:
    """Tests the get_identity method of JWTHandler."""
    handler = JWTHandler("testsecret")

    token = generate_test_token("testsecret", "user123", 3600)
    assert handler.get_identity(token) == "user123"

    invalid_token = token + "a"
    assert handler.get_identity(invalid_token) is None

    expired_token = generate_test_token("testsecret", "user123", -10)
    assert handler.get_identity(expired_token) is None
