# app/core/config.py
from pydantic_settings import BaseSettings
from pathlib import Path
import os

class Settings(BaseSettings):
    # Configuración de la API
    API_VERSION: str = "1.0.0"
    CORS_ORIGINS: str = "http://localhost:3000"
    
    # OpenAI
    OPENAI_API_KEY: str = None
    
    # GitHub
    GITHUB_TOKEN: str | None = None
    
    # Rutas
    UPLOAD_DIR: str = str(Path(__file__).parent.parent / "tmp_uploads")
    
    model_config = {
        "env_file": ".env",
        "extra": "allow"
    }

settings = Settings()

# Crear directorio de uploads si no existe
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)