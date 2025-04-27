from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_generate_exercise():
    response = client.post("/api/v1/exercises/generate", json={  # Corregido el endpoint
        "subject": "matemáticas",
        "difficulty": "fácil"
    })
    assert response.status_code == 200
    data = response.json()
    assert "generated_exercise" in data