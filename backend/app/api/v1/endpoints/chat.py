# app/api/v1/endpoints/chat.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.llm_service import get_ai_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    session_id: str  # Ahora necesitamos saber a qué "sesión" pertenece

class ChatResponse(BaseModel):
    response: str  # Cambiado de ai_response a response para coincidir con el test

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        ai_reply = await get_ai_response(
            message=request.message,
            session_id=request.session_id
        )
        return ChatResponse(response=ai_reply)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
