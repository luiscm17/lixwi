# app/api/v1/endpoints/exercise.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.crud.exercise import create_exercise, get_user_exercises
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.services.exercise_generator import generate_exercise

router = APIRouter()

# Esquema de entrada
class ExerciseCreate(BaseModel):
    user_id: int
    subject: str
    problem: str
    solution: Optional[str] = None
    difficulty: Optional[str] = "medium"

# Esquema de salida
class ExerciseOut(BaseModel):
    id: int
    user_id: int
    subject: str
    problem: str
    solution: Optional[str]
    difficulty: str
    created_at: datetime

    class Config:
        from_attributes = True  # Nuevo nombre para orm_mode en Pydantic v2

# Guardar un nuevo ejercicio
@router.post("/", response_model=ExerciseOut, summary="Guardar nuevo ejercicio", tags=["Exercises"])
def save_exercise(exercise: ExerciseCreate, db: Session = Depends(get_db)):
    try:
        db_exercise = create_exercise(
            db,
            user_id=exercise.user_id,
            subject=exercise.subject,
            problem=exercise.problem,
            solution=exercise.solution,
            difficulty=exercise.difficulty
        )
        return db_exercise
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al guardar ejercicio: {str(e)}")

# Listar ejercicios de un usuario
@router.get("/list/{user_id}", response_model=List[ExerciseOut], summary="Listar ejercicios de un usuario", tags=["Exercises"])
def list_exercises(user_id: int, db: Session = Depends(get_db)):
    try:
        exercises = get_user_exercises(db, user_id=user_id)
        return exercises
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al listar ejercicios: {str(e)}")


# Añadir el nuevo endpoint de generación
@router.post("/generate", summary="Generar nuevo ejercicio", tags=["Exercises"])
async def generate_exercise_endpoint(subject: str, difficulty: str, include_solution: bool = True):
    try:
        exercise = await generate_exercise(subject, difficulty, include_solution)
        return {"generated_exercise": exercise}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al generar ejercicio: {str(e)}")
