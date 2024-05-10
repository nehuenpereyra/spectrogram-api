from pydantic import BaseModel, EmailStr


class AllPathsResponse(BaseModel):
    fileName: str
    number_of_spectra: int
    saved: bool

    class Config:
        json_schema_extra = {
            "example": {
                "id": "64b9bbd3d0cfec0352b41a1c",
                "username": "test",
                "email": "test@test.com",
            }
        }
