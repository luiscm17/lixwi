# app/api/v1/schemas.py
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    ai_response: str

class UploadResponse(BaseModel):
    message: str
    filename: str

class VisualizationData(BaseModel):
    title: str
    x: list[int]
    y: list[int]
