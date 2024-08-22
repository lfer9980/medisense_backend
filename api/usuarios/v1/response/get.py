from uuid import uuid4
from pydantic import Field
from app.usuarios.enums import UserType

from core.base import BaseSchema


class GetUserResponse(BaseSchema):
    id: str
    avatar: str
    user_type: UserType

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": str(uuid4()),
                    "avatar": "/path/to/avatar.png",
                    "user_type": UserType.Paciente,
                }
            ]
        }
    }
