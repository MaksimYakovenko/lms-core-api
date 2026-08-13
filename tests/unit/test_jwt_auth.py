import pytest
from unittest.mock import MagicMock
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
import jwt
from src.middleware.jwt_auth import jwt_auth_middleware

@pytest.mark.asyncio
async def test_jwt_auth_middleware_valid_token():
    """Test that the middleware correctly sets the user state on a valid token."""
    mock_request = MagicMock(spec=Request)
    mock_request.headers = {"Authorization": "Bearer valid_token"}
    mock_request.state = MagicMock()

    secret = "testsecret"
    os.environ["JWT_SECRET"] = secret

    payload = {"user_id": "123"}
    encoded_token = jwt.encode(payload, secret, algorithm="HS256")
    mock_request.headers = {"Authorization": f"Bearer {encoded_token}"}

    mock_call_next = MagicMock(return_value=JSONResponse(content={}))

    response = await jwt_auth_middleware(mock_request, mock_call_next)

    assert response.status_code == 200
    assert mock_request.state.user == payload