from pydantic import BaseModel
from typing import TypeVar
from typing import Generic
from typing import Any

T = TypeVar("T")


class DefaultResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = 'success'
    data: T


def default_response(data: Any = None, message: str = "success", success: bool = True):
    return {
        "success": success,
        "message": message,
        "data": data
    }
