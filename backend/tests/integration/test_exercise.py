from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_save_exercise():
    response = client.post("/api/v1/exercises/", json={  # Corregido el endpoint
        "user_id": 1,
        "subject": "matemáticas",
        "problem": "¿Cuál es la raíz cuadrada de 16?",
        "solution": "4",
        "difficulty": "fácil"
    })
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "subject" in data