# app/core/config.py
from pydantic_settings import BaseSettings
from pathlib import Path
import os

class Settings(BaseSettings):
    # Configuración de la API
    API_VERSION: str
    CORS_ORIGINS: str
    
    # OpenAI
    OPENAI_API_KEY: str | None = None
    
    # GitHub
    GITHUB_TOKEN: str | None = None
    GITHUB_MODEL_ENDPOINT: str | None = None
    GITHUB_MODEL_NAME: str | None = None
    
    # Rutas
    UPLOAD_DIR: str = str(Path(__file__).parent.parent / "tmp_uploads")
    
    model_config = {
        "env_file": ".env",
        "extra": "allow"
    }

settings = Settings()

# Crear directorio de uploads si no existe
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)