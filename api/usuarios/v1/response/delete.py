from uuid import uuid4

from core.base import BaseSchema


class DeleteUserResponse(BaseSchema):
    id: str
    msg: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": str(uuid4()),
                    "msg": 'Usuario eliminado correctamente'
                }
            ]
        }
    }
