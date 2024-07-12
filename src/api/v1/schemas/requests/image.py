from pydantic import BaseModel, Field


class LoadRequest(BaseModel):
    img_name: str = Field(min_length=2, max_length=64)
    dir_path: str = Field(min_length=4, max_length=64)

    class Config:
        json_schema_extra = {
            "example": {
                "img_name": "H304",
                "dir_path": "C:/Users/User/Documents/db/"
            }
        }
