from fastapi import APIRouter, Depends

from api.auth.v1.request import LoginUserRequest
from api.auth.v1.response import LoginUserResponse

from core.db import create_session
from core.utils.token import create_access_token, create_refresh_token

auth_router = APIRouter()


@auth_router.post("/login")
async def login(request: LoginUserRequest,
                db=Depends(create_session)
                ) -> LoginUserResponse:

    token_data = create_access_token(user_id='1')
    refresh_token = create_refresh_token(user_id='1')

    data = {
        "access_token": token_data,
        "refresh_token": refresh_token,
        "token_type": 'bearer',
    }

    return LoginUserResponse.model_validate(data)
