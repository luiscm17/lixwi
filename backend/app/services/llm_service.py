# app/services/llm_service.py

import os
import logging
from openai import OpenAI
from app.core.config import settings
from app.core.memory import get_session_history, add_message_to_session
from app.core.prompts import format_system_prompt

# Configuración para GitHub Models
endpoint = settings.LLM_MODEL_ENDPOINT
model = settings.LLM_MODEL_NAME
api_key = settings.LLM_API_KEY

# Inicializar cliente OpenAI con configuración
client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

async def get_ai_response(message: str, session_id: str = None, execution_settings: dict = None) -> str:
    try:
        messages = []

        # Si hay session_id, manejamos historial
        if session_id:
            add_message_to_session(session_id, role="user", content=message)
            history = get_session_history(session_id)
            messages = [format_system_prompt()] + history
        else:
            # Sin historial (prompt aislado)
            messages = [{"role": "user", "content": message}]

        # Configuración del modelo
        chat_args = {
            "model": model,
            "messages": messages,
            "temperature": 1.0,
            "top_p": 1.0
        }

        # Si hay execution_settings, los aplicamos
        if execution_settings:
            chat_args.update(execution_settings)

        response = client.chat.completions.create(**chat_args)
        ai_message = response.choices[0].message.content.strip()

        if session_id:
            add_message_to_session(session_id, role="assistant", content=ai_message)

        return ai_message

    except Exception as e:
        logging.error(f"Error en LLM service: {str(e)}")
        return "Lo siento, hay un problema temporal. Por favor, intenta más tarde."
