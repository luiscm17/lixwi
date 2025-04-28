# app/core/logging_config.py
import logging
from logging.handlers import RotatingFileHandler
from app.core.config import settings

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(module)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            RotatingFileHandler(
                "app.log",
                maxBytes=1024*1024,  # 1MB
                backupCount=5,
                encoding="utf-8"
            )
        ]
    )
