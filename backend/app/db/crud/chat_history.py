from sqlalchemy.orm import Session
from app.db.models.chat_history import ChatHistory

def create_chat_history(db: Session, user_id: int, question: str, answer: str):
    db_chat = ChatHistory(user_id=user_id, question=question, answer=answer)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat

def get_user_chat_history(db: Session, user_id: int):
    return db.query(ChatHistory).filter(ChatHistory.user_id == user_id).all()