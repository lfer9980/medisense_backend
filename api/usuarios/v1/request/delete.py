from core.base import BaseSchema


class DeleteUserRequest(BaseSchema):
    password: str
    password_confirmation: str

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
