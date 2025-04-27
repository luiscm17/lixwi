# 🧠 Documentación Backend IA Tutor

---

# 1. `main.py`

## 🔎 Explicación

- Es el **punto de entrada** de toda la aplicación.
- Crea una instancia de `FastAPI`.
- Configura **routers** (rutas/endpoints).
- Configura **manejo de errores**.
- Configura el **logging**.

## 🔍 Conceptos Clave

- **FastAPI app instance**
- **Routers** para agrupar endpoints.
- **Exception Handlers** para capturar errores.
- **Middleware** para configuraciones extra (futuro).

## 🔹 Ejemplo:

```python
# app/main.py
from fastapi import FastAPI
from app.api.v1 import chat, upload, visualize
from app.api.v1 import error_handlers
from app.core.logging_config import setup_logging
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

setup_logging()

app = FastAPI()

app.include_router(chat.router)
app.include_router(upload.router)
app.include_router(visualize.router)

# Manejo de Errores Globales
app.add_exception_handler(RequestValidationError, error_handlers.validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, error_handlers.general_exception_handler)
```

---

# 2. `logging_config.py`

## 📅 Explicación

- Configura el sistema de **logging** para registrar eventos.
- Escribe logs tanto en **consola** como en **archivo** (`app.log`).

## 🔹 Ejemplo:

```python
# app/core/logging_config.py
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("app.log")
        ]
    )
```

## 📈 Beneficios

- Monitoreo del sistema.
- Detección de errores.
- Análisis de comportamiento.

---

# 3. `error_handlers.py`

## 💡 Explicación

- Define respuestas **personalizadas** cuando ocurre un error.
- Captura errores de validación y errores generales.

## 🔹 Ejemplo:

```python
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
```

---

# 4. `llm_service.py`

## 🔖 Explicación

- Servicio que se comunica con el **modelo OpenAI**.
- Envia mensaje del usuario y recibe respuesta de la IA.

## 🔹 Ejemplo:

```python
# app/services/llm_service.py
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def format_system_prompt():
    return {"role": "system", "content": "Eres un tutor experto que explica con claridad a estudiantes de ingeniería."}

async def get_ai_response(message: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                format_system_prompt(),
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error al generar respuesta: {str(e)}"
```

---

# 5. Endpoints `chat.py`, `upload.py`, `visualize.py`

## 5.1 `chat.py`

```python
# app/api/v1/chat.py
from fastapi import APIRouter
from app.services.llm_service import get_ai_response
from app.api.v1.schemas import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    response = await get_ai_response(request.message)
    return ChatResponse(ai_response=response)
```

## 5.2 `upload.py`

```python
# app/api/v1/upload.py
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.api.v1.schemas import UploadResponse
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload", response_model=UploadResponse)
async def upload_image(file: UploadFile = File(...)):
    try:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return UploadResponse(message="Archivo cargado correctamente.", filename=file.filename)
    except Exception as e:
        return JSONResponse(content={"message": f"Error al cargar archivo: {str(e)}"}, status_code=500)
```

## 5.3 `visualize.py`

```python
# app/api/v1/visualize.py
from fastapi import APIRouter
from app.api.v1.schemas import VisualizationData

router = APIRouter()

@router.get("/visualize", response_model=VisualizationData)
async def get_visualization():
    visualization_data = VisualizationData(
        title="Ejemplo de Gráfica",
        x=[1, 2, 3, 4, 5],
        y=[10, 20, 30, 40, 50]
    )
    return visualization_data
```

---

# 6. `schemas.py`

## 💡 Explicación

- Define **estructuras** de datos de entrada y salida.
- Valida automáticamente que los datos sean correctos.

## 🔹 Ejemplo:

```python
# app/api/v1/schemas.py
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    ai_response: str

class UploadResponse(BaseModel):
    message: str
    filename: str

class VisualizationData(BaseModel):
    title: str
    x: list[int]
    y: list[int]
```

---

# 📈 Conceptos sugeridos para estudiar

- **Pydantic Schemas**
- **FastAPI Response Models**
- **OpenAPI Specification**
- **Swagger UI**
- **Logging en Python**
- **Decoradores en Python**

---

# 📆 Referencias importantes

- [FastAPI - Error Handling](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [FastAPI - Response Model](https://fastapi.tiangolo.com/tutorial/response-model/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [OpenAI Python Migration Guide](https://github.com/openai/openai-python/discussions/742)
- [Swagger UI Info](https://swagger.io/tools/swagger-ui/)

---

# ✅ Estado Actual del Proyecto

- 🔹 Backend modularizado.
- 🔹 Endpoints funcionando.
- 🔹 Logging implementado.
- 🔹 Manejo de errores implementado.
- 🔹 API documentada automáticamente en Swagger UI.

---