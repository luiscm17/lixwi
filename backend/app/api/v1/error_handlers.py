from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
import logging

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logging.error(f"Error de validación: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": [{"loc": err["loc"], "msg": err["msg"]} for err in exc.errors()]}
    )

async def database_exception_handler(request: Request, exc: SQLAlchemyError):
    logging.error(f"Error de base de datos: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Error interno de base de datos"}
    )

async def general_exception_handler(request: Request, exc: Exception):
    logging.error(f"Error general: {str(exc)}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Error interno del servidor"}
    )
