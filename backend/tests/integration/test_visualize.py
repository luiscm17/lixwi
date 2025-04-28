from fastapi.testclient import TestClient
from app.main import app
import pytest
import numpy as np

client = TestClient(app)

def test_basic_expression():
    response = client.get("/api/v1/visualize/?expression=2*x+1&x_range=-5,5")
    assert response.status_code == 200
    data = response.json()
    assert "x" in data
    assert "y" in data
    assert "title" in data
    assert len(data["x"]) == 100  # Verificar número de puntos
    assert len(data["y"]) == 100

def test_trigonometric_expression():
    response = client.get("/api/v1/visualize/?expression=sen(x)&x_range=-3.14,3.14")
    assert response.status_code == 200
    data = response.json()
    assert "x" in data
    assert "y" in data
    assert max(data["y"]) <= 1.0
    assert min(data["y"]) >= -1.0

def test_custom_variable():
    response = client.get("/api/v1/visualize/?expression=2*t+1&x_range=-5,5&variable=t")
    assert response.status_code == 200
    data = response.json()
    assert data["variable"] == "t"

def test_invalid_expression():
    response = client.get("/api/v1/visualize/?expression=invalid&x_range=-5,5")
    assert response.status_code == 400

def test_invalid_range():
    response = client.get("/api/v1/visualize/?expression=x&x_range=5,-5")
    assert response.status_code == 400
    assert "valor inicial del rango debe ser menor" in response.json()["detail"]

def test_complex_expression():
    response = client.get("/api/v1/visualize/?expression=(x+1)(x-1)&x_range=-2,2")
    assert response.status_code == 200
    data = response.json()
    assert "x" in data
    assert "y" in data

def test_infinite_values():
    response = client.get("/api/v1/visualize/?expression=1/x&x_range=-1,1")
    assert response.status_code == 400
    assert "valores infinitos" in response.json()["detail"]

def test_implicit_multiplication():
    response = client.get("/api/v1/visualize/?expression=2x+1&x_range=-5,5")
    assert response.status_code == 200
    data = response.json()
    assert "x" in data
    assert "y" in data
    # Verificar algunos puntos específicos
    x_values = data["x"]
    y_values = data["y"]
    # y debe ser 2x + 1
    for i in range(len(x_values)):
        assert abs(y_values[i] - (2 * x_values[i] + 1)) < 1e-10

def test_nested_parentheses():
    response = client.get("/api/v1/visualize/?expression=(2(x+1))^2&x_range=-5,5")
    assert response.status_code == 200
    data = response.json()
    assert "x" in data
    assert "y" in data

def test_spanish_function_names():
    response = client.get("/api/v1/visualize/?expression=seno(x)+coseno(x)&x_range=-3.14,3.14")
    assert response.status_code == 200
    data = response.json()
    assert "x" in data
    assert "y" in data
    # La suma de seno y coseno debe estar entre -√2 y √2
    assert all(-1.5 <= y <= 1.5 for y in data["y"])

def test_invalid_variable_name():
    response = client.get("/api/v1/visualize/?expression=2x+1&x_range=-5,5&variable=123")
    assert response.status_code == 400
    assert "identificador válido" in response.json()["detail"]