from app.db.session import Base, engine
from app.db.models.user import User
from app.db.models.chat_history import ChatHistory
from app.db.models.exercise import Exercise

print("Creando todas las tablas en la base de datos...")

Base.metadata.create_all(bind=engine)

print("¡Tablas creadas exitosamente!")
