from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from src.config import Settings
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.controllers import user, workspace
from src.core.exception_handlers import CustomException, custom_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.core import default_response

settings = Settings()


def create_application() -> FastAPI:
    """
    Create the FastAPI application v1
    """

    app = FastAPI(docs_url=None if settings.STAGE == 'production' else '/docs')

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOW_ORIGINS.split(','),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # add routers/controllers
    app.include_router(user.router)
    app.include_router(workspace.router)

    # add exception handlers and middleware
    app.add_exception_handler(
        CustomException, custom_exception_handler)

    return app


app: FastAPI = create_application()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(default_response(
            data={"errors": exc.errors()}, message="Unprocessable Entity", success=False)),
    )
