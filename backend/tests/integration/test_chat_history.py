from fastapi.testclient import TestClient
from app.main import app
from app.db.models.chat_history import ChatMessage

def test_chat_history_save(client):
    response = client.post("/api/v1/chat_history/chat/save/", json={
        "session_id": "test_session",
        "message": "Hola",
        "user_id": 1,
        "role": "user"
    })
    assert response.status_code == 200
    assert "message_id" in response.json()

def test_invalid_chat_history(client):
    response = client.post("/api/v1/chat_history/chat/save/", json={
        "session_id": "",  # ID de sesión vacío
        "message": "Hola",
        "user_id": 1,
        "role": "invalid_role"  # Rol inválido
    })
    assert response.status_code == 400

def test_get_chat_history(client):
    # Primero guardamos un mensaje
    save_response = client.post("/api/v1/chat_history/chat/save/", json={
        "session_id": "test_session",
        "message": "Hola",
        "user_id": 1,
        "role": "user"
    })
    assert save_response.status_code == 200

    # Luego obtenemos el historial
    response = client.get("/api/v1/chat_history/session/test_session")
    assert response.status_code == 200
    messages = response.json()
    assert isinstance(messages, list)
    assert len(messages) > 0