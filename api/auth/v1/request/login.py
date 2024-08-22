from uuid import uuid4
from pydantic import (Field,
                      EmailStr,
                      SecretStr
                      )

from core.base import BaseSchema


class LoginUserRequest(BaseSchema):
    id: str = Field(default_factory=lambda: str(uuid4()))
    email: EmailStr
    password: SecretStr

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "test@test.com",
                    "password": "<PASSWORD>",
                }
            ]
        }
    }
