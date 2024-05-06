from fastapi import APIRouter
from typing import List
from src.core import default_response, DefaultResponse
from src.api.v1.schemas import UserResponse
from src.decorators import exception


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {
        "success": False,
        "message": "Not found",
        "Data": None
    }}
)

exception_info = {
    "moduleName": "user",
    "fullpath": __name__
}


@router.get("", response_model=DefaultResponse[List[UserResponse]])
@exception(functName='all_users', **exception_info)
async def all_users():
    users = []
    return default_response(data=users)
