from fastapi import FastAPI
from src.api.v1.app import app as app_v1
from smallthon import sm_list


def create_application() -> FastAPI:
    """
    Create the FastAPI application
    """

    sm_list()

    application = FastAPI()

    application.mount("/api/v1", app_v1)

    return application


app: FastAPI = create_application()
