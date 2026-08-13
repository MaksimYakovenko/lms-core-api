import pytest
from jwt import ExpiredSignatureError, DecodeError
from unittest.mock import patch
from src.jwt_utils import validate_jwt_token, JWTUtility, JWTClaims

def test_validate_jwt_token_valid():
    token = "valid.token.here"
    secret_key = "secret_key"
    expected_payload = {"exp": 12345, "claim_key": "claim_value"}
    
    with patch("jwt.decode", return_value=expected_payload):
        result = validate_jwt_token(token, secret_key)
        assert result == expected_payload

def test_validate_jwt_token_expired():
    token = "expired.token.here"
    secret_key = "secret_key"
    
    with patch("jwt.decode", side_effect=ExpiredSignatureError):
        with pytest.raises(ValueError, match="Token has expired"):
            validate_jwt_token(token, secret_key)

def test_validate_jwt_token_invalid():
    token = "invalid.token.here"
    secret_key = "secret_key"
    
    with patch("jwt.decode", side_effect=DecodeError):
        with pytest.raises(ValueError, match="Token is invalid"):
            validate_jwt_token(token, secret_key)

def test_extract_claims():
    token = "valid.token.here"
    secret_key = "secret_key"
    decoded_payload = {"exp": 12345, "claim_key": "claim_value"}

    with patch("src.jwt_utils.validate_jwt_token", return_value=decoded_payload):
        claims = JWTUtility.extract_claims(token, secret_key)
        assert isinstance(claims, JWTClaims)
        assert claims.exp == 12345
        assert claims.additional_claims == {"claim_key": "claim_value"}