from http import HTTPStatus
from fastapi import HTTPException
from sqlalchemy.orm import Session, Query

from core.utils.hasher import Hasher
from core.base.crud import BaseCRUD

from app.models.usuarios import UserModel
from app.usuarios.schemas import *


class UserCommands(BaseCRUD):

    @classmethod
    async def create(cls, db: Session, user: dict) -> UserModel:

        user = CreateUserSchema.model_validate(user)

        email_exists: Query = await cls._filter_by(
            db=db,
            filters={
                'email': user.email
            },
            model=UserModel
        )
        if email_exists.first():
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Email ya registrado'
            )

        phone_exists: Query = await cls._filter_by(
            db=db,
            filters={'phone': user.phone},
            model=UserModel
        )
        if phone_exists.first():
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Celular ya registrado'
            )

        hashed_password = Hasher.get_password_hash(user.password)
        user_data = user.model_dump()
        user_data.pop('password_confirmation', None)
        user_data['password'] = hashed_password

        db_user = UserModel(**user_data)

        await cls._save(db, db_user)
        return db_user

    @classmethod
    async def update(cls, db: Session, new_data_user: dict, user_id: str) -> UserModel:

        new_data_user = UpdateUserSchema.model_validate(new_data_user)

        original_user: UserModel = await cls._get_by_id(
            db=db,
            model=UserModel,
            this_id=user_id
        )

        if not Hasher.verify_password(plain_password=new_data_user.old_password,
                                      hashed_password=original_user.password):
            raise HTTPException(
                detail='Password incorrect',
                status_code=HTTPStatus.CONFLICT
            )

        if new_data_user.new_email:
            email_exists: Query = await cls._filter_by(
                db=db,
                filters={'email': new_data_user.new_email},
                model=UserModel
            )
            if email_exists.first() and email_exists.first().id != user_id:
                raise HTTPException(
                    status_code=HTTPStatus.CONFLICT,
                    detail='Email ya registrado'
                )

        if new_data_user.new_phone:
            phone_exists: Query = await cls._filter_by(
                db=db,
                filters={'phone': new_data_user.get('phone')},
                model=UserModel
            )
            if phone_exists.first() and phone_exists.first().id != user_id:
                raise HTTPException(
                    status_code=HTTPStatus.CONFLICT,
                    detail='Celular ya registrado'
                )

        new_user = new_data_user.model_dump()

        if new_data_user.new_password:
            hashed_password = Hasher.get_password_hash(new_data_user.new_password)
            new_user['password'] = hashed_password

        for key, value in new_user.items():
            if value is not None:
                setattr(original_user, key, value)

        await cls._update(db=db,
                          data=original_user)

        return original_user

    @classmethod
    async def delete(cls, db: Session, user_id: str, delete_user_data: dict) -> None:

        delete_user_data = DeleteUserSchema.model_validate(delete_user_data)

        user: UserModel = await cls._get_by_id(
            db=db,
            model=UserModel,
            this_id=user_id
        )

        if not Hasher.verify_password(plain_password=delete_user_data.password,
                                      hashed_password=user.password):
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Password incorrect'
            )

        await cls._delete(db=db,
                          data=user)
