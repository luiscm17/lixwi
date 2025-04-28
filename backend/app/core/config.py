# app/core/config.py
from pydantic_settings import BaseSettings
from pathlib import Path
import os

class Settings(BaseSettings):
    # Configuración de la API
    API_VERSION: str = "v1"
    CORS_ORIGINS: List[str] = []
    
    # LLM Configuration
    LLM_API_KEY: str | None = None
    LLM_MODEL_ENDPOINT: str | None = None
    LLM_MODEL_NAME: str | None = None
    
    # Database
    DATABASE_URL: str
    
    # Rutas
    UPLOAD_DIR: str = str(Path(__file__).parent.parent / "tmp_uploads")
    
    model_config = {
        "env_file": ".env",
        "extra": "allow"
    }

settings = Settings()

# Crear directorio de uploads si no existe
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)