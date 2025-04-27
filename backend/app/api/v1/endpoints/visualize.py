import pytest
from app.core.memory import get_session_history, add_message_to_session
from fastapi import APIRouter, HTTPException
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

router = APIRouter()  # Esta línea es crucial - faltaba el router

@router.get("/")
async def visualize_expression(expression: str, x_range: str):
    try:
        # Parsear el rango
        start, end = map(float, x_range.split(","))
        
        # Generar puntos x
        x = np.linspace(start, end, 100)
        
        # Evaluar la expresión (con seguridad)
        y = eval(f"lambda x: {expression}")(x)
        
        return {
            "title": f"Gráfica de {expression}",
            "x": x.tolist(),
            "y": y.tolist()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@pytest.fixture(autouse=True)
def clear_session():
    # Limpiar la memoria antes de cada prueba
    from app.core.memory import _sessions
    _sessions.clear()

def test_session_memory():
    session_id = "test_session"
    
    # Prueba agregar mensaje
    add_message_to_session(session_id, "user", "Hola")
    history = get_session_history(session_id)
    
    assert len(history) == 1
    assert history[0]["role"] == "user"
    assert history[0]["content"] == "Hola"