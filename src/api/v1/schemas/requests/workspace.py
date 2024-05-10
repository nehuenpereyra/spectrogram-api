from pydantic import BaseModel


class AllPathsRequest(BaseModel):
    path_dir: str

    class Config:
        json_schema_extra = {
            "example": {
                "path_dir": ""
            }
        }
