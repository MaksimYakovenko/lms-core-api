from __future__ import annotations

import jwt
from jwt import DecodeError, ExpiredSignatureError, InvalidTokenError
from typing import TypedDict

class JWTClaims(TypedDict):
    exp: int
    [key: str]: str | int | bool  # Allow for custom claims

def validate_jwt_token(token: str, secret_key: str) -> dict[str, str | int | bool]:
    """
    Validates a JWT token's signature and decodes its payload if valid.

    Args:
        token: The JWT token string to validate and parse.
        secret_key: The secret key used for signature validation.

    Returns:
        A dictionary containing the decoded JWT payload.
    
    Raises:
        jwt.exceptions.ExpiredSignatureError: If the token signature has expired.
        jwt.exceptions.InvalidTokenError: If the token is invalid.
    """
    try:
        return jwt.decode(token, secret_key, algorithms=['HS256'], options={"require": ["exp"]})
    except ExpiredSignatureError as e:
        raise ValueError("Token has expired.") from e
    except InvalidTokenError as e:
        raise ValueError("Token is invalid.") from e
