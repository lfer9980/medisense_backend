from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from core.utils.token import decode_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:

    payload = decode_jwt(token)
    user_id: str = payload.get("user_id")

    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    token_data = {"user_id": user_id}

    return token_data
