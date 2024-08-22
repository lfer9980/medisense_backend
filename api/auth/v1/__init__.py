from fastapi import APIRouter

from .routes import auth_router

sub_router = APIRouter(prefix="/v1")
sub_router.include_router(auth_router,
                          prefix="/auth",
                          tags=["Authentication"])


__all__ = ["sub_router"]
