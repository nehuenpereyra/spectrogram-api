import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_users(client: AsyncClient):
    response = await client.get("/api/v1/users")
    res_json = response.json()
    assert response.status_code == 200
    assert "success" in res_json and res_json["success"] == True
