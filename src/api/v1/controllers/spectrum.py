from fastapi import APIRouter
from typing import List
from src.core import default_response, DefaultResponse
from src.api.v1.schemas import PredictRequest, PredictionsResponse
from src.api.v1.services import workspace
from src.decorators import exception
from src.api.v1.services import spectrum

router = APIRouter(
    prefix="/spectrum",
    tags=["spectrum"],
    responses={404: {
        "success": False,
        "message": "Not found",
        "Data": None
    }}
)

exception_info = {
    "moduleName": "spectrum",
    "fullpath": __name__
}


@router.post("/predict", response_model=DefaultResponse[PredictionsResponse])
@exception(functName='predict', **exception_info)
async def predict(data: PredictRequest):
    return default_response(data=spectrum.predict(data))
