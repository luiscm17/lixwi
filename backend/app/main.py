from fastapi import FastAPI, Depends, APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.v1.endpoints import chat, upload, visualize, generate
from app.core.config import settings  # Asume que config.py tiene una clase `Settings`
from app.core.logging_config import setup_logging
from app.api.v1 import error_handlers
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.api.v1.endpoints import user
from app.api.v1.endpoints import chat_history
from app.api.v1.endpoints import exercise

# Configura logging primero
setup_logging()

app = FastAPI(
    title="IA Tutor API",
    description="Backend para un agente de tutoría inteligente especializado en matemáticas",
    version=settings.API_VERSION,  # Ej: "1.0.0" desde variables de entorno
    docs_url="/docs",  # Habilitar Swagger UI
    redoc_url=None,  # Deshabilitar ReDoc si no se usa
)

# --- Middlewares ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS.split(","),  # Ej: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
api_router.include_router(generate.router, prefix="/generate", tags=["Generate"]) 
api_router.include_router(user.router, prefix="/users", tags=["Users"]) 
api_router.include_router(chat_history.router, prefix="/chat_history", tags=["Chat History"])
api_router.include_router(exercise.router, prefix="/exercise", tags=["Exercise"])
app.include_router(api_router)

# --- Ruta de Salud ---
@app.get("/health", include_in_schema=False)
def health_check():
    return {"status": "healthy", "version": settings.API_VERSION}

# --- Ruta Raíz ---
@app.get("/")
def root():
    return {
        "message": "Bienvenido a IA Tutor API 🚀", 
        "docs": "/docs",
        "endpoints": ["/api/v1/chat", "/api/v1/upload", "/api/v1/visualize"]
    }