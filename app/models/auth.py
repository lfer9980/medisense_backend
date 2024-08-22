from sqlalchemy import (Column, String)

from core.base import BaseTable


class TokenModel(BaseTable):
    __tablename__ = 'tokens'

    token = Column(String, index=True)
    user_id = Column(String)
