from fastapi import Request
from fastapi.responses import JSONResponse
from typing import Dict, Any


class CustomException(Exception):
    def __init__(self,
                 status_code: int,
                 message: str = None,
                 headers: Dict[str, Any] | None = None):
        self.status_code = status_code
        self.data = {
            "success": False,
            "message": message,
            "data": None
        }
        self.headers = headers


async def custom_exception_handler(request: Request, exc: CustomException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.data,
        headers=exc.headers
    )
