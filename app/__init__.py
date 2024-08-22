from fastapi import FastAPI

from core import (VERSION,
                  OPEN_API_TITLE,
                  OPEN_API_DESCRIPTION)
from core.settings import settings
from core.base import BaseResponse
from core.fastapi import (init_cors,
                          init_routers,
                          init_listeners)


def create_app() -> FastAPI:
    app = FastAPI(
        version=VERSION,
        title=OPEN_API_TITLE,
        description=OPEN_API_DESCRIPTION,
        swager_url="/",
        docs_url=None if settings.ENV == "production" else "/",
        redoc_url=None if settings.ENV == "production" else "/redoc",
        openapi_url=None if settings.ENV == "production" else "/openapi.json",
        debug=False if settings.ENV == "production" else True,
    )

    init_cors(app=app)
    init_routers(app=app)
    init_listeners(app=app)

    return app


app = create_app()
