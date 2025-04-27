import pytest
from unittest.mock import Mock, patch
from app.services.llm_service import get_ai_response

@pytest.mark.asyncio
async def test_get_ai_response_success():
    mock_response = Mock()
    mock_response.choices = [Mock(message=Mock(content="Respuesta de prueba"))]
    
    with patch('app.services.llm_service.client.chat.completions.create', 
                return_value=mock_response):
        response = await get_ai_response("¿Pregunta?", "test_session")
        assert isinstance(response, str)
        assert len(response) > 0

@pytest.mark.asyncio
async def test_get_ai_response_error():
    with patch('app.services.llm_service.client.chat.completions.create', 
                side_effect=Exception("Error de API")):
        response = await get_ai_response("¿Pregunta?", "test_session")
        assert response == "Lo siento, hay un problema temporal. Por favor, intenta más tarde."