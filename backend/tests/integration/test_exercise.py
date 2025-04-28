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

def test_list_exercises():
    # Primero creamos un ejercicio
    exercise_data = {
        "user_id": 1,
        "subject": "matemáticas",
        "problem": "¿Cuál es la derivada de x^2?",
        "solution": "2x",
        "difficulty": "medio"
    }
    client.post("/api/v1/exercises/", json=exercise_data)
    
    # Luego obtenemos la lista
    response = client.get("/api/v1/exercises/list/1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "subject" in data[0]
    assert "problem" in data[0]

def test_invalid_exercise_data():
    invalid_data = {
        "user_id": "no_numerico",  # Debería ser un número
        "subject": "matemáticas",
        "problem": "¿Cuál es la raíz cuadrada de 16?",
        "difficulty": "fácil"
    }
    response = client.post("/api/v1/exercises/", json=invalid_data)
    assert response.status_code == 400  # Cambiado de 422 a 400
    assert "detail" in response.json()

def test_generate_exercise_with_solution():
    response = client.post("/api/v1/exercises/generate", json={
        "subject": "matemáticas",
        "difficulty": "fácil",
        "include_solution": True
    })
    assert response.status_code == 200
    data = response.json()
    assert "generated_exercise" in data
    assert isinstance(data["generated_exercise"], dict)