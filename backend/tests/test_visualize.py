import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_visualization():
    response = client.get("/api/v1/visualize", params={
        "expression": "x**2",  # Cambiado de x^2 a x**2 para sintaxis Python
        "x_range": "-10,10"
    })
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert "x" in data
    assert "y" in data