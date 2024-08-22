from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def init_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,  # noqa
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
