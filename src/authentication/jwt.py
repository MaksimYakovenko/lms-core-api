from __future__ import annotations

import jwt
from datetime import datetime
from typing import Any, cast, dict

class JWTHandler:
    """
    A class for handling JWT operations like validation and user identity extraction.
    """

    def __init__(self, secret: str):
        """
        Initialize the JWTHandler with a given secret for encoding and decoding JWTs.
        
        Parameters:
        secret: str - The secret key used for decoding.
        """
        self._secret = secret

    def validate_token(self, token: str) -> bool:
        """
        Validates the given JWT.
        
        Parameters:
        token: str - The JWT token to validate.
        
        Returns:
        bool - True if the token is valid, False otherwise.
        """
        try:
            decoded = jwt.decode(token, self._secret, algorithms=["HS256"])
            return "sub" in decoded and "exp" in decoded and datetime.fromtimestamp(decoded["exp"]) > datetime.now()
        except (jwt.InvalidTokenError, KeyError):
            return False

    def get_identity(self, token: str) -> str | None:
        """
        Extracts the user identity from a given JWT.
        
        Parameters:
        token: str - The JWT token from which to extract the identity.
        
        Returns:
        str | None - The user identity if present and valid, otherwise None.
        """
        try:
            decoded = jwt.decode(token, self._secret, algorithms=["HS256"])
            return cast(str, decoded.get("sub"))
        except (jwt.InvalidTokenError, KeyError):
            return None
