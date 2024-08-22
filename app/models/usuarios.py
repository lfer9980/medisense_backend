import datetime
from sqlalchemy import (Column, String, Enum, Boolean, DateTime)

from app.usuarios.enums import UserType
from core.base import BaseTable


class UserModel(BaseTable):
    __tablename__ = 'usuarios'

    email = Column(String,
                   unique=True,
                   nullable=False)
    phone = Column(String,
                   unique=True,
                   nullable=False)
    password = Column(String,
                      nullable=False)
    user_type = Column(Enum(UserType),
                       nullable=False,
                       default=UserType.Paciente)
    avatar = Column(String,
                    unique=True,
                    nullable=True)
    is_active = Column(Boolean,
                       default=False)
    is_verified = Column(Boolean,
                         default=False)

    created_at = Column(DateTime,
                        default=datetime.datetime.now(datetime.timezone.utc))

