from __future__ import annotations

import pytest
import time
import jwt
from src.jwt_utils import validate_jwt_token

SECRET_KEY = "my_secret_key"

@pytest.fixture
def generate_token() -> str:
    payload = {
        "exp": int(time.time()) + 60,
        "username": "test_user",
        "role": "admin"
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def test_validate_jwt_token_success(generate_token: str) -> None:
    token = generate_token
    expected_payload = {"exp": pytest.approx(time.time() + 60, rel=1), "username": "test_user", "role": "admin"}
    result = validate_jwt_token(token, SECRET_KEY)
    assert result["username"] == expected_payload["username"]
    assert result["role"] == expected_payload["role"]

def test_validate_jwt_token_expired() -> None:
    expired_payload = {"exp": int(time.time()) - 10, "username": "expired_user"}
    token = jwt.encode(expired_payload, SECRET_KEY, algorithm='HS256')
    with pytest.raises(ValueError, match="Token has expired"):
        validate_jwt_token(token, SECRET_KEY)

def test_validate_jwt_token_invalid() -> None:
    invalid_token = "invalidtoken"
    with pytest.raises(ValueError, match="Token is invalid"):
        validate_jwt_token(invalid_token, SECRET_KEY)
