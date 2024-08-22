from uuid import uuid4
from pydantic import EmailStr
from app.usuarios.enums import UserType

from core.base import BaseSchema


class UpdateUserResponse(BaseSchema):
    id: str
    email: EmailStr
    phone: str
    avatar: str
    user_type: UserType

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": str(uuid4()),
                    "email": "<EMAIL>",
                    "phone": "0123456789",
                    "avatar": "/path/to/avatar.png",
                    "user_type": UserType.Paciente,
                }
            ]
        }
    }
