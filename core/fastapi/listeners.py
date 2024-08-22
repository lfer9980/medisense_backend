from fastapi import FastAPI, Request
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError

from core.base import BaseResponse


def init_listeners(app: FastAPI) -> None:
    async def http_exception_handler(request, exc: HTTPException):
        response = {
            'status_code': exc.status_code,
            'errors': {f'{exc.status_code}': exc.detail},
            'content': {},
        }

        return BaseResponse(**response)

    async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        inputs = [input_data['loc'][-1] for input_data in exc.errors()]
        messages = [error['msg'] for error in exc.errors()]

        response = {
            'status_code': 422,
            'errors': dict(zip(inputs, messages)),
            'content': {}
        }

        return BaseResponse(**response)

    async def response_exception_handler(request: Request, exc: HTTPException):
        response = {
            'status_code': 422,
            'errors': {f'{exc.status_code}': exc.detail},
            'content': {}
        }

        return BaseResponse(**response)

    # app.add_exception_handler(HTTPException,
    #                           http_exception_handler)  # noqa
    #
    # app.add_exception_handler(RequestValidationError,
    #                           request_validation_exception_handler)  # noqa
    #
    # app.add_exception_handler(ValueError,
    #                           response_exception_handler) # noqa