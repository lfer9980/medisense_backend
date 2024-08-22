from fastapi import APIRouter

from .routes import user_router

sub_router = APIRouter(prefix="/v1")
sub_router.include_router(user_router,
                          prefix="/usuarios",
                          tags=["User"])


__all__ = ["sub_router"]
