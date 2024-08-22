from fastapi import HTTPException
from pydantic import field_validator

from core.base import BaseSchema


class DeleteUserSchema(BaseSchema):
    password: str
    password_confirmation: str

    @field_validator('password_confirmation')
    @classmethod
    def is_valid_password_confirmation(cls, password_confirmation: str, data) -> None:
        if password_confirmation != data.data['password']:
            raise HTTPException(
                status_code=400,
                detail='Passwords do not match',
            )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "password": "<PASSWORD>",
                    "password_confirmation": "<PASSWORD>",
                }
            ]
        }
    }
