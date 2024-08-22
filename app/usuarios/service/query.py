from sqlalchemy.orm import Session
from core.base.crud import BaseCRUD

from app.models.usuarios import UserModel


class UserQuery(BaseCRUD):

    @classmethod
    async def get_user_by_id(cls, user_id: str, db: Session) -> UserModel:

        user: UserModel = await cls._get_by_id(
            this_id=user_id,
            db=db,
            model=UserModel,
        )

        return user
