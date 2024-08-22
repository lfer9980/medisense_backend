from core.base import BaseSchema


class LoginUserResponse(BaseSchema):

    access_token: str
    token_type: str = 'bearer'
    refresh_token: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "access_token": "<ACCES_TOKEN_HERE>",
                    "token_type": "Bearer",
                    "refresh_token": "<REFRESH_TOKEN_HERE>",
                }
            ]
        }
    }
