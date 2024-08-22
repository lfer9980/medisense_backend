from fastapi import FastAPI

from api import router
from core import API_PREFIX


def init_routers(app: FastAPI) -> None:
    app.include_router(router,
                       prefix=API_PREFIX)
