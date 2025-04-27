from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_chat_history_save():
    response = client.post("/api/v1/chat_history/chat/save/", json={
        "session_id": "test_session",
        "message": "Hola",
        "user_id": 1,  # Campo requerido que faltaba
        "role": "user"  # Campo requerido que faltaba
    })
    assert response.status_code == 200
    assert "status" in response.json()