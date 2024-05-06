from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr

    class Config:
        json_schema_extra = {
            "example": {
                "id": "64b9bbd3d0cfec0352b41a1c",
                "username": "test",
                "email": "test@test.com",
            }
        }
