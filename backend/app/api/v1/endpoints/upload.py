# app/api/v1/endpoints/upload.py
from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from app.services.image_processing import extract_text_from_image  # Nueva función
from app.utils.validators import is_math_problem  # Validador opcional

router = APIRouter()
UPLOAD_DIR = "./tmp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    if len(await file.read()) > 5 * 1024 * 1024:  # 5MB límite
        raise HTTPException(status_code=400, detail="Archivo demasiado grande")
    await file.seek(0)  # Resetear el cursor del archivo
    # Validar tipo y extensión
    allowed_types = ["image/png", "image/jpeg", "image/jpg"]
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Formato no soportado. Use PNG/JPEG.")
    
    # Guardar imagen
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Extraer texto (OCR)
    try:
        extracted_text = extract_text_from_image(file_path)  # Implementar esto
        if not is_math_problem(extracted_text):  # Opcional: validar contenido
            raise HTTPException(status_code=400, detail="La imagen no contiene un problema matemático válido.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen: {str(e)}")
    
    return {
        "filename": file.filename,
        "extracted_text": extracted_text,  # Añadir texto extraído
        "message": "Imagen procesada exitosamente"
    }