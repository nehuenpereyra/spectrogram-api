
import os
import cv2
from src.api.v1.schemas import PredictRequest
import base64
from src.api.v1.services.workspace import get_config_path
from src.helpers.DictPersistJSON import DictPersistJSON


def load(data: PredictRequest):

    dir_path = data.img_path
    img_name = data.img_name
    filename = os.path.join(data.img_path, data.img_name)

    if not os.path.exists(filename):
        raise ValueError(f"El archivo {filename} no existe.")

    print('Step 1')
    img_info = cv2.imread(filename, -1)
    img = cv2.imread(filename)

    original_dtype = img_info.dtype
    original_height, original_width, _ = img.shape

    if not (img_name.split(sep='.')[-1] == 'png'):
        if ((original_width < original_height)):
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        original_height, original_width, _ = img.shape
        filename = os.path.join(dir_path, 'train', img_name+'.png')
        if not os.path.exists(os.path.join(dir_path, 'train')):
            os.mkdir(os.path.join(dir_path, 'train'))
        # cv2.imwrite(filename, img, [cv2.IMWRITE_JPEG_QUALITY, 50])
        # <- Hay una reduccion implicita del 95% en la calidad de la imagen
        cv2.imwrite(filename, img)

    with open(filename, "rb") as f:
        image_binary = f.read()

    image = base64.b64encode(image_binary).decode("utf-8")

    # Make data for return mesagge
    data = {
        'status': True,
        'image': image,
        'info': {
            'width': original_width,
            'heigth': original_height,
            "name": img_name.split(sep=".")[0],
            "ext": img_name.split(sep=".")[-1],
            "path": os.path.join(dir_path, img_name),
            "dtype": str(original_dtype)
        }
    }

    # It checks if there is information saved for that image and
    # if it exists it adds its information to data
    saved_path = os.path.join(get_config_path(), 'cache', 'saved')
    working_path = os.path.join(get_config_path(), 'cache', 'working')
    if not os.path.exists(saved_path):
        os.mkdir(saved_path)
    if not os.path.exists(working_path):
        os.mkdir(working_path)
    saved_path = os.path.join(saved_path, img_name+".json")
    working_path = os.path.join(working_path, img_name+".json")

    if (os.path.isfile(working_path) or os.path.isfile(saved_path)):
        if (os.path.isfile(working_path)):
            dataList = DictPersistJSON(working_path)["body"]
        else:
            dataList = DictPersistJSON(saved_path)["body"]

        print(dataList)
        bbox = dataList["bbox_arr"]
        plateData = dataList["plate_data"]
        metadata = dataList["data_arr"]
        data["info"]["bboxes"] = bbox
        data["info"]["metadata"] = metadata
        data["info"]["plateData"] = plateData

    # api response data
    print('Data', data)
    return data
