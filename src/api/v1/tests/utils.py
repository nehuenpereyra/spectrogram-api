from httpx import AsyncClient


async def get_first_user(client: AsyncClient, auth: dict[str, str]):
    response = await client.get("/api/v1/users", headers=auth)
    res_json = response.json()
    return res_json["data"][0]
