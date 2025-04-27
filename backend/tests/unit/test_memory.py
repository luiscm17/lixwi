import pytest
from app.core.memory import get_session_history, add_message_to_session

@pytest.fixture(autouse=True)
def clear_session():
    # Limpiar la memoria antes de cada prueba
    from app.core.memory import _sessions
    _sessions.clear()

def test_session_memory():
    session_id = "test_session"
    
    # Prueba agregar mensaje
    add_message_to_session(session_id, "user", "Hola")
    history = get_session_history(session_id)
    
    assert len(history) == 1
    assert history[0]["role"] == "user"
    assert history[0]["content"] == "Hola"