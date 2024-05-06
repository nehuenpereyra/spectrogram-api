
from fastapi import FastAPI
from asgi_lifespan import LifespanManager
from httpx import AsyncClient, ASGITransport
import pytest
from .main import create_application
from src.config import get_settings

settings = get_settings()
settings.STAGE = 'test'

app: FastAPI = create_application()


@pytest.fixture()
async def client():
    """
    Create an instance of the client.
    :return: yield HTTP client.
    """
    async with LifespanManager(app):

        async with AsyncClient(transport=ASGITransport(app), base_url="http://test", follow_redirects=True) as ac:
            try:
                yield ac
            except Exception as exc:  # pylint: disable=broad-except
                print(exc)
