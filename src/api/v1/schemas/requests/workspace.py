from pydantic import BaseModel
from typing import List
from typing import Optional, List


class AllPathsRequest(BaseModel):
    path_dir: str

    class Config:
        json_schema_extra = {
            "example": {
                "path_dir": ""
            }
        }


class SaveConfigRequest(BaseModel):
    global_config: Optional[dict] = None
    fields: Optional[dict] = None

    class Config:
        json_schema_extra = {
            "example": {
                "global_config": {
                    "workspace_path": "./db/"
                },
                "fields": {
                    "OBSERVAT": {
                        "options": [
                            "ctio: Cerro Tololo Interamerican Observatory",
                        ]
                    }
                }
            }
        }
