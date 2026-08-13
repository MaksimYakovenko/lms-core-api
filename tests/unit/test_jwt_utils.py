from __future__ import annotations

import pytest
import time
import jwt
from src.jwt_utils import validate_jwt_token, JWTUtility, JWTClaims

SECRET_KEY = "my_super_secret_key"

@pytest.fixture
def generate_valid_token() -> str:
    """Generates a valid JWT token for testing purposes."""
    payload = {
        "exp": int(time.time()) + 60,
        "username": "test_user",
        "role": "admin"
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def test_validate_jwt_token_success(generate_valid_token: str) -> None:
    """Tests successful decoding of a valid JWT token."""
    token = generate_valid_token
    result = validate_jwt_token(token, SECRET_KEY)
    assert result["username"] == "test_user"
    assert result["role"] == "admin"

def test_validate_jwt_token_expired() -> None:
    """Tests decoding of an expired JWT token raises ValueError."""
    expired_payload = {
        "exp": int(time.time()) - 10,
        "username": "expired_user"
    }
    token = jwt.encode(expired_payload, SECRET_KEY, algorithm='HS256')
    with pytest.raises(ValueError, match="Token has expired"):
        validate_jwt_token(token, SECRET_KEY)

def test_validate_jwt_token_invalid() -> None:
    """Tests decoding of an invalid JWT token raises ValueError."""
    invalid_token = "invalid.token.string"
    with pytest.raises(ValueError, match="Token is invalid"):
        validate_jwt_token(invalid_token, SECRET_KEY)

def test_extract_claims_success(generate_valid_token: str) -> None:
    """Tests extraction of claims from a valid JWT token."""
    token = generate_valid_token
    extracted_claims = JWTUtility.extract_claims(token, SECRET_KEY)
    assert isinstance(extracted_claims, JWTClaims)
    assert extracted_claims.exp >= int(time.time())
    assert extracted_claims.additional_claims["username"] == "test_user"
    assert extracted_claims.additional_claims["role"] == "admin"
