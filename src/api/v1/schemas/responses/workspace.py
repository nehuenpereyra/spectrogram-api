from pydantic import BaseModel, EmailStr


class AllPathsResponse(BaseModel):
    fileName: str
    number_of_spectra: int
    saved: bool

    class Config:
        json_schema_extra = {
            "example": {
                "fileName": "H304.tif",
                "number_of_spectra": 0,
                "saved": True,
            }
        }


class ConfigResponse(BaseModel):

    global_config: dict
    fields: dict

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
