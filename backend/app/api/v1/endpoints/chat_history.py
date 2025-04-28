# app/api/v1/endpoints/chat_history.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models.chat_history import ChatMessage
from app.db.models.user import User
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

router = APIRouter()

class ChatMessageCreate(BaseModel):
    session_id: str
    message: str
    user_id: int
    role: str

    model_config = ConfigDict(from_attributes=True)

class ChatMessageResponse(BaseModel):
    id: int
    session_id: str
    message: str
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

@router.post("/", response_model=dict)
async def save_chat_message(chat_data: ChatMessageCreate, db: Session = Depends(get_db)):
    try:
        if not chat_data.session_id.strip():
            raise HTTPException(status_code=400, detail="El ID de sesión no puede estar vacío")
        
        if chat_data.role not in ['user', 'assistant']:
            raise HTTPException(status_code=400, detail="Rol inválido. Debe ser 'user' o 'assistant'")
        
        user = db.query(User).filter(User.id == chat_data.user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        db_message = ChatMessage(
            session_id=chat_data.session_id,
            message=chat_data.message,
            user_id=chat_data.user_id,
            role=chat_data.role
        )
        
        db.add(db_message)
        db.commit()
        db.refresh(db_message)
        
        return {"status": "success", "message_id": db_message.id}
        
    except HTTPException as he:
        raise he
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@router.get("/{session_id}", response_model=List[ChatMessageResponse])
async def get_chat_history(session_id: str, db: Session = Depends(get_db)):
    try:
        if not session_id.strip():
            raise HTTPException(status_code=400, detail="El ID de sesión no puede estar vacío")
            
        messages = db.query(ChatMessage).filter(
            ChatMessage.session_id == session_id
        ).order_by(ChatMessage.created_at).all()
        
        return messages
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener historial: {str(e)}")
