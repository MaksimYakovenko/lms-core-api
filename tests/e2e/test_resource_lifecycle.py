import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_crud_group(client: AsyncClient, auth_headers: dict):
    response = await client.post(
        "/groups/create_group",
        json={"name": "Test Group", "course_number": 101},
        headers=auth_headers,
    )
    assert response.status_code == 200
    created_group = response.json()

    group_id = created_group["id"]

    response = await client.put(
        f"/groups/update_group/{group_id}",
        json={"name": "Updated Group", "course_number": 102},
        headers=auth_headers,
    )
    assert response.status_code == 200

    response = await client.delete(f"/groups/delete_group/{group_id}", headers=auth_headers)
    assert response.status_code == 200