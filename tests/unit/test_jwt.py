import pytest
import jwt
from unittest.mock import patch
from datetime import datetime, timedelta
from src.authentication.jwt import JWTHandler

def generate_test_token(secret: str, sub: str = None, exp_delta: timedelta = None) -> str:
    payload = {}
    if sub:
        payload["sub"] = sub
    if exp_delta:
        payload["exp"] = int((datetime.now() + exp_delta).timestamp())
    return jwt.encode(payload, secret, algorithm="HS256")

def test_validate_token_valid():
    secret = "testsecret"
    handler = JWTHandler(secret)
    token = generate_test_token(secret, sub="testuser", exp_delta=timedelta(days=1))
    assert handler.validate_token(token) is True

def test_validate_token_expired():
    secret = "testsecret"
    handler = JWTHandler(secret)
    token = generate_test_token(secret, sub="testuser", exp_delta=timedelta(seconds=-1))
    assert handler.validate_token(token) is False

def test_validate_token_invalid_signature():
    secret = "testsecret"
    wrong_secret = "wrongsecret"
    handler = JWTHandler(secret)
    token = generate_test_token(wrong_secret, sub="testuser", exp_delta=timedelta(days=1))
    assert handler.validate_token(token) is False

def test_get_identity_valid():
    secret = "testsecret"
    handler = JWTHandler(secret)
    token = generate_test_token(secret, sub="testuser", exp_delta=timedelta(days=1))
    assert handler.get_identity(token) == "testuser"

def test_get_identity_invalid_token():
    secret = "testsecret"
    handler = JWTHandler(secret)
    token = "invalid_token"
    assert handler.get_identity(token) is None

def test_get_identity_missing_sub():
    secret = "testsecret"
    handler = JWTHandler(secret)
    token = generate_test_token(secret, exp_delta=timedelta(days=1))
    assert handler.get_identity(token) is None