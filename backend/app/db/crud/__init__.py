# Importar todas las funciones CRUD para que estén disponibles al importar el paquete
from .user import create_user, get_user
from .chat_history import create_chat_history, get_user_chat_history
from .exercise import create_exercise, get_user_exercises

__all__ = [
    'create_user', 'get_user',
    'create_chat_history', 'get_user_chat_history',
    'create_exercise', 'get_user_exercises'
]