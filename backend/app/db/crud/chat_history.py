from sqlalchemy.orm import Session
from app.db.models.chat_history import ChatMessage
from typing import List

def create_chat_message(db: Session, session_id: str, user_id: int, message: str, role: str) -> ChatMessage:
    db_message = ChatMessage(
        session_id=session_id,
        user_id=user_id,
        message=message,
        role=role
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_session_messages(db: Session, session_id: str) -> List[ChatMessage]:
    return db.query(ChatMessage).filter(
        ChatMessage.session_id == session_id
    ).order_by(ChatMessage.created_at).all()