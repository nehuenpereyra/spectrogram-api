from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    img_name: str = Field(min_length=2, max_length=64)
    img_path: str = Field(min_length=4, max_length=64)

    class Config:
        json_schema_extra = {
            "example": {
                "img_name": "",
                "img_path": ""
            }
        }
