from fastapi import FastAPI, Depends, APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.v1.endpoints import chat, upload, visualize
from app.core.config import settings  # Asume que config.py tiene una clase `Settings`
from app.core.logging_config import setup_logging
from app.api.v1 import error_handlers
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.api.v1.endpoints import user
from app.api.v1.endpoints import chat_history
from app.api.v1.endpoints import exercise
from app.api.v1.endpoints import agent

# Configura logging primero
setup_logging()

app = FastAPI(
    title="Lixwi AI",
    description="Backend para un agente de tutoría inteligente especializado en matemáticas",
    version=settings.API_VERSION,  # Ej: "1.0.0" desde variables de entorno
    docs_url="/docs",  # Habilitar Swagger UI
    redoc_url=None,  # Deshabilitar ReDoc si no se usa
)

# --- Middlewares ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
    expose_headers=["Content-Length"],
    max_age=600,
)

# --- Manejo de Errores ---
app.add_exception_handler(RequestValidationError, error_handlers.validation_exception_handler)
app.add_exception_handler(StarletteHTTPException, error_handlers.general_exception_handler)

# --- Rutas Estáticas (para imágenes subidas) ---
app.mount("/tmp_uploads", StaticFiles(directory="tmp_uploads"), name="uploads")

# --- Incluir Routers ---
api_router = APIRouter(prefix="/api/v1")
api_router.include_router(chat.router, prefix="/chat", tags=["Chat"])
api_router.include_router(upload.router, prefix="/upload", tags=["Upload"])
api_router.include_router(visualize.router, prefix="/visualize", tags=["Visualize"])
api_router.include_router(user.router, prefix="/users", tags=["Users"]) 
api_router.include_router(chat_history.router, prefix="/chat_history", tags=["Chat History"])
api_router.include_router(exercise.router, prefix="/exercises", tags=["Exercises"])  
api_router.include_router(agent.router, prefix="/agent", tags=["Agent"])    
app.include_router(api_router)

# --- Ruta de Salud ---
@app.get("/health", include_in_schema=False)
def health_check():
    return {"status": "healthy", "version": settings.API_VERSION}

# --- Ruta Raíz ---
@app.get("/")
def root():
    return {
        "message": "Bienvenido a Lixwi AI 🚀", 
        "docs": "/docs",
        "endpoints": ["/api/v1/chat", "/api/v1/upload", "/api/v1/visualize"]
    }
