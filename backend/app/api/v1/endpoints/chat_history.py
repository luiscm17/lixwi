# app/api/v1/endpoints/chat_history.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.crud.chat_history import create_chat_history
from pydantic import BaseModel

router = APIRouter()

# Esquema de entrada
class ChatCreate(BaseModel):
    user_id: int
    question: str
    answer: str

@router.post("/chat/save/", summary="Guardar mensaje en historial", tags=["Chat History"])
def save_chat(chat: ChatCreate, db: Session = Depends(get_db)):
    try:
        saved_chat = create_chat_history(db, user_id=chat.user_id, question=chat.question, answer=chat.answer)
        return {
            "id": saved_chat.id,
            "user_id": saved_chat.user_id,
            "question": saved_chat.question,
            "answer": saved_chat.answer,
            "created_at": saved_chat.created_at
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al guardar historial: {str(e)}")
