import re
import datetime
from typing import Any

from uuid import uuid4

from fastapi import HTTPException
from pydantic import Field, EmailStr, field_validator

from app.usuarios.utils import password_regex, phone_regex
from app.usuarios.enums import UserType

from core.base import BaseSchema


class CreateUserSchema(BaseSchema):
    id: str = Field(default_factory=lambda: str(uuid4()))
    email: EmailStr
    phone: str
    password: str
    password_confirmation: str
    user_type: UserType
    avatar: str = None
    created_at: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))

    @field_validator('password')
    @classmethod
    def is_valid_password(cls, password: str) -> str:
        if not re.match(pattern=password_regex, string=password):
            raise HTTPException(
                status_code=400,
                detail='Password must match pattern'
            )
        return password

    @field_validator('phone')
    @classmethod
    def is_valid_phone(cls, phone: str) -> str:
        if not re.match(pattern=phone_regex, string=phone):
            raise HTTPException(
                status_code=400,
                detail='Phone must match pattern'
            )
        return phone

    @field_validator('password_confirmation')
    @classmethod
    def is_valid_password_confirmation(cls, password_confirmation: str, data) -> None:
        if password_confirmation != data.data['password']:
            raise HTTPException(
                status_code=400,
                detail='Passwords do not match',
            )
