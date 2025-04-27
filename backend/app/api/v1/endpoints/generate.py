# app/api/v1/endpoints/generate.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.exercise_generator import generate_exercise

router = APIRouter()

class ExerciseRequest(BaseModel):
    subject: str
    difficulty: str
    include_solution: bool = True  

@router.post("/generate-exercise")
async def generate_exercise_endpoint(request: ExerciseRequest):
    exercise = await generate_exercise(request.subject, request.difficulty, request.include_solution)
    return {"generated_exercise": exercise}
