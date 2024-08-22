import jwt
from typing import Optional
from fastapi import HTTPException, Request
from datetime import datetime, timedelta, UTC
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, ExpiredSignatureError

from core.settings import settings


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)

        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")

            token = credentials.credentials
            if not self.verify_jwt(token):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")

            return token
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    @staticmethod
    def verify_jwt(token: str) -> bool:
        try:
            decode_jwt(token)
            return True

        except ExpiredSignatureError:
            return False

        except JWTError:
            return False


def create_access_token(user_id: str) -> str:
    expires_delta = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode = {"expire": expires_delta, "user_id": user_id}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt


def create_refresh_token(user_id: str, ) -> str:
    expires_delta = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"expire": expires_delta, "user_id": user_id}
    encoded_jwt = jwt.encode(to_encode, settings.REFRESH_SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt


def decode_jwt(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        return payload
    except jwt.exceptions.InvalidTokenError:
        return None
