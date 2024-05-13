from fastapi import APIRouter
from typing import List
from src.core import default_response, DefaultResponse
from src.api.v1.schemas import AllPathsResponse, SaveConfigRequest, ConfigResponse
from src.api.v1.services import workspace
from src.decorators import exception

router = APIRouter(
    prefix="/workspace",
    tags=["workspace"],
    responses={404: {
        "success": False,
        "message": "Not found",
        "Data": None
    }}
)

exception_info = {
    "moduleName": "workspace",
    "fullpath": __name__
}


@router.get("/allPaths", response_model=DefaultResponse[List[AllPathsResponse]])
@exception(functName='all_paths', **exception_info)
async def all_paths(path_dir: str = None):

    if path_dir == None:
        raise ValueError('Se requiere enviar el parametro all_paths')

    return default_response(data=workspace.get_all_paths(path_dir))


@router.get("/loadConfig", response_model=DefaultResponse[ConfigResponse])
@exception(functName='load_config', **exception_info)
async def load_config():
    return default_response(data=workspace.api_load_config())


@router.post("/saveConfig", response_model=DefaultResponse[None])
@exception(functName='save_config', **exception_info)
async def save_config(newConfig: SaveConfigRequest):
    workspace.api_save_config(newConfig)
    return default_response(data=None)
