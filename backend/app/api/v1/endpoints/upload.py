# app/api/v1/endpoints/upload.py
from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from app.services.image_processing import extract_text_from_image
from app.utils.validators import is_math_problem

router = APIRouter()
UPLOAD_DIR = "./tmp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Validar tamaño
        content = await file.read()
        if len(content) > 5 * 1024 * 1024:  # 5MB
            raise HTTPException(status_code=400, detail="Archivo demasiado grande")
            
        # Validar formato
        if file.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(status_code=400, detail="Formato no soportado")
            
        # Guardar archivo
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(content)
            
        return {"filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))