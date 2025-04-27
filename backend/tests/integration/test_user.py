from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_user_creation():
    test_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "TestPassword123!"
    }
    
    response = client.post("/api/v1/users/", json=test_data)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["username"] == test_data["username"]
    assert data["email"] == test_data["email"]