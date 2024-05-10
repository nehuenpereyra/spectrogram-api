import os
from fastapi import APIRouter
from typing import List
from src.core import default_response, DefaultResponse
from src.api.v1.schemas import AllPathsResponse
from src.decorators import exception
from src.helpers import DictPersistJSON
from pathlib import Path
from ..services.config import get_workspace_path

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


@router.get("allPaths", response_model=DefaultResponse[List[AllPathsResponse]])
@exception(functName='all_paths', **exception_info)
async def all_paths(path_dir: str = None):

    if path_dir == None:
        raise ValueError('Se requiere enviar el parametro all_paths')

    path_dir = Path(path_dir).expanduser().absolute()
    print(path_dir)
    if not path_dir.exists():
        raise ValueError('No existe el directorio')

    all_paths = os.listdir(path_dir)

    # formats = ['png', 'tif', 'tiff']
    formats = ['tiff', 'tif']
    all_paths = all_paths.select(
        lambda item: item.split(sep='.').last() in formats)

    # Separates the names of the files of which information is stored in the cache
    cache_path = os.path.join(get_workspace_path(), 'cache')
    working_path = aux_path = os.path.join(cache_path, 'working')
    saved_path = aux_path = os.path.join(cache_path, 'saved')

    if not os.path.exists(cache_path):
        os.mkdir(cache_path)
        os.mkdir(working_path)
        os.mkdir(saved_path)
    else:
        if not os.path.exists(working_path):
            os.mkdir(working_path)
        if not os.path.exists(saved_path):
            os.mkdir(saved_path)

    # Removes .json extensions
    working_files = [file_name[:-5] for file_name in os.listdir(working_path)]

    saved_files = [file_name[:-5] for file_name in os.listdir(saved_path)]  # R

    # Counts the number of spectra in each file
    paths = []

    for i, file in enumerate(all_paths):
        paths.append({
            "fileName": file,
            "number_of_spectra": 0,
            "saved": False
        })
        if (file in working_files):
            aux_path = os.path.join(working_path, file+".json")
            paths[i]["saved"] = True
            paths[i]["number_of_spectra"] = len(
                DictPersistJSON(aux_path)["body"]["bbox_arr"])
        elif (file in saved_files):
            paths[i]["saved"] = True
            paths[i]["number_of_spectra"] = -1

    return default_response(data=paths)
