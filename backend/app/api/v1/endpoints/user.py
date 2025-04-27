# app/api/v1/endpoints/user.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.crud.user import create_user
from pydantic import BaseModel

router = APIRouter()

# Esquema de entrada
class UserCreate(BaseModel):
    username: str
    email: str = None

@router.post("/users/", summary="Crear nuevo usuario", tags=["Users"])
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(db, username=user.username, email=user.email)
        return {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email,
            "created_at": new_user.created_at
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear usuario: {str(e)}")
