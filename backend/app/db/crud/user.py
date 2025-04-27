from sqlalchemy.orm import Session
from app.db.models.user import User

def create_user(db: Session, username: str, email: str = None):
    db_user = User(username=username, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

