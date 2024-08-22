import datetime
from uuid import uuid4
from pydantic import Field, EmailStr

from app.usuarios.enums import UserType

from core.base import BaseSchema


class CreateUserRequest(BaseSchema):
    id: str = Field(default_factory=lambda: str(uuid4()))
    email: EmailStr
    phone: str
    password: str
    password_confirmation: str
    user_type: UserType
    avatar: str = None
    created_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "hide@hide.com",
                    "phone": "6251241954",
                    "password": "pw",
                    "password_confirmation": "pw",
                    "user_type": UserType.Paciente,
                    "avatar": "path/to/avatar.png",
                    "created_at": datetime.datetime.now(),
                }
            ]
        }
    }
