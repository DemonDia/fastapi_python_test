from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from config import app
# SOURCE: https://github.com/tiangolo/fastapi/issues/484
@app.exception_handler(ValidationError)
async def handler1(request: Request, exc: Exception):
    print("ValidationError")
    print(type(exc))
    return JSONResponse(str(exc))


@app.exception_handler(RequestValidationError)
async def handler2(request: Request, exc: Exception):
    print("RequestValidationError")
    print(type(exc))
    return JSONResponse(str(exc))


@app.exception_handler(Exception)
async def handler3(request: Request, exc: Exception):
    print("Exception")
    print(type(exc))
    return JSONResponse(str(exc))