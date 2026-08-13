from __future__ import annotations

from fastapi.testclient import TestClient
from src.endpoints.authenticated_profile import router

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_get_profile_valid_token(mocker) -> None:
    valid_user_id = "test_user_id"
    token = jwt.encode({"user_id": valid_user_id}, key="test_secret", algorithm="HS256")

    mocker.patch("src.endpoints.authenticated_profile.decode_jwt_token", return_value={"user_id": valid_user_id})
    mocker.patch("src.endpoints.authenticated_profile.retrieve_user_profile",
                 return_value={"id": valid_user_id, "name": "Test User", "email": "test@example.com"})

    response = client.get("/profile", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    json_response = response.json()
    assert json_response["id"] == valid_user_id
    assert response.json() == {"id": valid_user_id, "name": "Test User", "email": "test@example.com"}
