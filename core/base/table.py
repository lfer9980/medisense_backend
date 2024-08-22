import uuid
from sqlalchemy import (Column, String)

from core.db.definitions import SQLModel


class BaseTable(SQLModel):
    __abstract__ = True

    id = Column(String,
                name='id',
                default=lambda: str(uuid.uuid4()),
                primary_key=True,
                )
