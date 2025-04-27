# app/models/chat.py
from pydantic import BaseModel

class ChatRequest(BaseModel):
    user_message: str

class ChatResponse(BaseModel):
    ai_response: str
