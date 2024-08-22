from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from core.db import create_session

from app.usuarios.service import UserCommands, UserQuery

from api.usuarios.v1.request import *
from api.usuarios.v1.response import *

user_router = APIRouter()


@user_router.post("/create", summary="Create User")
async def create_user(request: CreateUserRequest,
                      db: Session = Depends(create_session)
                      ) -> CreateUserResponse:

    new_user = CreateUserRequest.model_validate(request)

    user = await UserCommands.create(
        db=db,
        user=CreateUserRequest.model_dump(new_user),
    )

    return CreateUserResponse.model_validate(user)


@user_router.put("/update/{user_id}", summary="Updates User")
async def update_user(user_id: str,
                      request: UpdateUserRequest,
                      db: Session = Depends(create_session)) -> UpdateUserResponse:

    user = await UserCommands.update(
        db=db,
        user_id=user_id,
        new_data_user=UpdateUserRequest.model_dump(request)
    )

    return UpdateUserResponse.model_validate(user)


@user_router.delete("/delete/{user_id}", summary="Deletes User")
async def delete_user(user_id: str,
                      request: DeleteUserRequest,
                      db: Session = Depends(create_session)
                      ) -> DeleteUserResponse:

    await UserCommands().delete(
        db=db,
        user_id=user_id,
        delete_user_data=DeleteUserRequest.model_dump(request)
    )

    data = {
        'id': user_id,
        'msg': 'usuario eliminado correctamente'
    }

    return DeleteUserResponse.model_validate(data)


@user_router.get("/get/{user_id}", summary="Get current usuarios")
async def get_current_user(user_id: str,
                           db: Session = Depends(create_session)) -> GetUserResponse:

    user = await UserQuery().get_user_by_id(
        user_id=user_id,
        db=db
    )

    return GetUserResponse.model_validate(user)
