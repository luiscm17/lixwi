# app/api/v1/error_handlers.py
from fastapi import Request
from fastapi.responses import JSONResponse

async def validation_exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=400,
        content={"message": "Error de validación de datos."}
    )

async def general_exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Error interno del servidor."}
    )
