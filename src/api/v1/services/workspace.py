import os
import json
from pathlib import Path
from src.helpers import DictPersistJSON


CONFIG_FOLDERNAME = "config"
CONFIG_FILENAME = "db.json"


def get_config_folder():
    path = Path('static') / CONFIG_FOLDERNAME
    path = path.expanduser().absolute()
    path.mkdir(exist_ok=True, parents=True)
    return path


def get_config_path():
    return get_config_folder() / CONFIG_FILENAME


def api_save_config(config):
    config_aux = {}
    save_path = get_config_path()
    print(f"Saving config to {save_path}")
    config_aux["config"] = config.__dict__
    with open(save_path, 'w') as file:
        json.dump(config_aux, file, indent=4)
    return True


def api_load_config():

    path = get_config_path()
    print(f"Using config path: {path}")
    config = {}

    if path.is_file():
        with open(path, 'r') as file:
            config = json.load(file)["config"]
    else:
        raise Exception(f"File {path} does not exist")

    return config


def get_all_paths(path_dir):

    path_dir = Path(path_dir).expanduser().absolute()

    if not path_dir.exists():
        raise ValueError('No existe el directorio')

    all_paths = os.listdir(path_dir)

    # formats = ['png', 'tif', 'tiff']
    formats = ['tiff', 'tif']
    all_paths = all_paths.select(
        lambda item: item.split(sep='.').last() in formats)

    # Separates the names of the files of which information is stored in the cache
    cache_path = os.path.join(
        api_load_config()['global_config']['workspace_path'], 'cache')
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

    return paths
