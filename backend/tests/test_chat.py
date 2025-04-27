from fastapi.testclient import TestClient
from app.main import app
import pytest
from unittest.mock import patch

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Bienvenido a IA Tutor API 🚀",
        "docs": "/docs",
        "endpoints": ["/api/v1/chat", "/api/v1/upload", "/api/v1/visualize"]
    }

@pytest.mark.asyncio
async def test_chat_endpoint():
    # Mock del servicio LLM para evitar llamadas reales
    mock_response = "Respuesta de prueba"
    with patch('app.services.llm_service.get_ai_response', return_value=mock_response):
        response = client.post(
            "/api/v1/chat/",
            json={
                "message": "Hola",
                "session_id": "test_session"
            }
        )
        if response.status_code != 200:
            print(f"Error response: {response.json()}")
        assert response.status_code == 200
        assert "response" in response.json()