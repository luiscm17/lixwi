# app/services/llm_service.py

import os
import logging
from openai import OpenAI
from app.core.config import settings
from app.core.memory import get_session_history, add_message_to_session
from app.core.prompts import format_system_prompt

# Configuración para GitHub Models
endpoint = settings.GITHUB_MODEL_ENDPOINT
model = settings.GITHUB_MODEL_NAME

# Inicializar cliente OpenAI con configuración
client = OpenAI(
    base_url=endpoint,
    api_key=settings.GITHUB_TOKEN
)

async def get_ai_response(message: str, session_id: str) -> str:
    try:
        # Guardamos el mensaje del usuario
        add_message_to_session(session_id, role="user", content=message)

        # Obtenemos historial
        history = get_session_history(session_id)

        # Preparamos mensajes (prompt + historial)
        messages = [format_system_prompt()] + history

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=1.0,
            top_p=1.0
        )

        ai_message = response.choices[0].message.content.strip()

        # Guardamos respuesta IA
        add_message_to_session(session_id, role="assistant", content=ai_message)

        return ai_message
    except Exception as e:
        logging.error(f"Error en LLM service: {str(e)}")
        return "Lo siento, hay un problema temporal. Por favor, intenta más tarde."
