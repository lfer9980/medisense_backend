from typing import Optional
from pydantic import EmailStr

from core.base import BaseSchema


class UpdateUserRequest(BaseSchema):
    old_password: str
    new_email: Optional[EmailStr]
    new_phone: Optional[str]
    new_password: Optional[str]
    new_password_confirmation: Optional[str]
    new_avatar: Optional[str]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "new_email": "newhide@hide.com",
                    "new_phone": "6251241955",
                    "old_password": "pw",
                    "new_password": "Xx.sf23s2g4.xX",
                    "new_password_confirmation": "Xx.sf23s2g4.xX",
                    "new_avatar": "path/to/new_avatar.png",
                }
            ]
        }
    }
