from pydantic import BaseModel, EmailStr, model_validator
from typing import Optional


class UserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "username": "test",
                "email": "test@test.com",
                "password": "123456",
                "role": "Admin"
            }
        }


class UserUpdateRequest(BaseModel):
    id: str
    username: Optional[str]
    email: Optional[EmailStr]
    role: Optional[str]

    @model_validator(mode="before")
    def check_update(cls, values):
        if (values.get('username') is None) and (values.get("email") is None) and (values.get("role") is None):
            raise ValueError('Send at least one attribute to update')
        return values

    class Config:
        json_schema_extra = {
            "example": {
                "id": "64b9bbd3d0cfec0352b41a1c",
                "username": "test",
                "email": "test@test.com",
                "role": "Admin"
            }
        }


class UserUpdatePasswordRequest(BaseModel):
    current_password: str
    new_password: str

    class Config:
        json_schema_extra = {
            "example": {
                "current_password": "123456",
                "new_password": "SecurePass99."
            }
        }
