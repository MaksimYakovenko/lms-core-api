from __future__ import annotations

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# Mock function to get user data
def get_user_data(username: str) -> dict[str, str]:
    users = {
        "john_doe": {"name": "John Doe", "email": "john_doe@example.com"},
        "jane_doe": {"name": "Jane Doe", "email": "jane_doe@example.com"},
    }
    return users.get(username, None)

# OAuth2 setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock function to simulate token validation and user identification
def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    user_tokens = {
        "valid_token_john": "john_doe",
        "valid_token_jane": "jane_doe",
    }
    return user_tokens.get(token, None)

@app.get("/api/profile", response_model=dict[str, str])
def profile_endpoint(user: str = Depends(get_current_user)) -> dict[str, str]:
    """Endpoint to retrieve profile information for the authenticated user."""
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    user_data = get_user_data(user)
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data
