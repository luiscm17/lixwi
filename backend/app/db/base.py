from app.db.session import Base

# No importar los modelos aquí para evitar importaciones circulares
from app.db.models.user import User
from app.db.models.chat_history import ChatHistory
from app.db.models.exercise import Exercise

# Todas las tablas estarán disponibles en 'Base.metadata.tables'