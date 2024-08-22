import re
from typing import Optional
from fastapi import HTTPException
from pydantic import field_validator, EmailStr, ValidationError

from app.usuarios.utils import password_regex, phone_regex

from core.base import BaseSchema


class UpdateUserSchema(BaseSchema):
    old_password: str
    new_email: Optional[EmailStr]
    new_phone: Optional[str]
    new_password: Optional[str]
    new_password_confirmation: Optional[str]
    new_avatar: Optional[str]

    @field_validator('new_password')
    @classmethod
    def is_valid_password(cls, new_password: str) -> str:
        if new_password and not re.match(pattern=password_regex, string=new_password):
            raise HTTPException(
                status_code=400,
                detail='Password must match pattern'
            )
        return new_password

    @field_validator('new_phone')
    @classmethod
    def is_valid_phone(cls, new_phone: str) -> str:
        if new_phone and not re.match(pattern=phone_regex, string=new_phone):
            raise HTTPException(
                status_code=400,
                detail='Phone must match pattern'
            )
        return new_phone

    @field_validator('new_password_confirmation')
    @classmethod
    def is_valid_password_confirmation(cls, new_password_confirmation: str, data) -> None:
        if new_password_confirmation != data.data['new_password']:
            raise HTTPException(
                status_code=400,
                detail='Passwords do not match',
            )
