# app/core/logging_config.py
import logging
from logging.handlers import RotatingFileHandler

# Configuración básica de logging
def setup_logging():
    handlers = [
        logging.StreamHandler(),
        RotatingFileHandler("app.log", maxBytes=1024*1024, backupCount=5)
    ]
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),   # Mostrar en consola
            logging.FileHandler("app.log")  # Guardar en archivo 'app.log'
        ]
    )
