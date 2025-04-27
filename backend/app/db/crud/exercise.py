from sqlalchemy.orm import Session
from app.db.models.exercise import Exercise

def create_exercise(db: Session, user_id: int, subject: str, problem: str, solution: str = None, difficulty: str = "medium"):
    db_exercise = Exercise(
        user_id=user_id,
        subject=subject,
        problem=problem,
        solution=solution,
        difficulty=difficulty
    )
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

def get_user_exercises(db: Session, user_id: int):
    return db.query(Exercise).filter(Exercise.user_id == user_id).all()