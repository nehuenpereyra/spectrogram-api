from fastapi import APIRouter
from src.core import default_response, DefaultResponse
from src.api.v1.schemas import PredictRequest
from src.decorators import exception
from src.api.v1.services import image

router = APIRouter(
    prefix="/image",
    tags=["image"],
    responses={404: {
        "success": False,
        "message": "Not found",
        "Data": None
    }}
)

exception_info = {
    "moduleName": "image",
    "fullpath": __name__
}


@router.post("/load", response_model=DefaultResponse[None])
@exception(functName='load_img', **exception_info)
async def load_img(data: PredictRequest):
    return default_response(data=image.load(data))
