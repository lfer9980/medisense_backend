from fastapi import APIRouter

from api.usuarios.v1 import sub_router as user_v1_router
from api.auth.v1 import sub_router as auth_v1_router

router = APIRouter()
router.include_router(user_v1_router)
router.include_router(auth_v1_router)


__all__ = ["router"]
