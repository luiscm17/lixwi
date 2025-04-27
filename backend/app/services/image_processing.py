# app/services/image_processing.py
import easyocr
import os
from typing import Optional

def extract_text_from_image(image_path: str, languages: list = ['es', 'en']) -> Optional[str]:
    """
    Extrae texto de una imagen usando OCR.
    
    Args:
        image_path (str): Ruta al archivo de imagen.
        languages (list): Idiomas para el OCR (ej: ['es', 'en']).

    Returns:
        str: Texto extraído o None si falla.
    """
    try:
        reader = easyocr.Reader(languages)
        result = reader.readtext(image_path)
        return " ".join([text for (_, text, _) in result])
    except Exception as e:
        print(f"❌ Error en OCR: {e}")
        return None