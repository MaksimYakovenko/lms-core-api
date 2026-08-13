from __future__ import annotations

import jwt
from jwt import DecodeError, ExpiredSignatureError, InvalidTokenError

class JWTClaims:
    """Represents a decoded claims structure."""
    exp: int
    additional_claims: dict[str, str | int | bool]

def validate_jwt_token(token: str, secret_key: str) -> dict[str, str | int | bool]:
    """Validates a JWT token's signature and decodes its payload if the signature matches.

    Parameters:
    token (str): The JWT token string to validate and parse.
    secret_key (str): The secret key used for signature validation.

    Returns:
    dict[str, str | int | bool]: A dictionary containing the decoded JWT payload.

    Raises:
    ValueError: If the token is invalid or has expired.
    """
    try:
        return jwt.decode(token, secret_key, algorithms=['HS256'], options={"require": ["exp"]})
    except ExpiredSignatureError as e:
        raise ValueError("Token has expired.") from e
    except DecodeError as e:
        raise ValueError("Token is invalid.") from e

class JWTUtility:
    """Utility class for JWT operations."""

    @staticmethod
    def extract_claims(token: str, secret_key: str) -> JWTClaims:
        """Extracts claims from the provided JWT Token.

        Parameters:
        token (str): The JWT token string to extract claims from.
        secret_key (str): The secret key used for decoding.

        Returns:
        JWTClaims: A structure containing the decoded claims.
        """
        payload = validate_jwt_token(token, secret_key)
        claims = JWTClaims(exp=payload.pop('exp'), additional_claims=payload)
        return claims
