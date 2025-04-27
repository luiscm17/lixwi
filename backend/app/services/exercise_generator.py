# app/services/exercise_generator.py

from app.services.llm_service import client
import os

model = "openai/gpt-4o"

async def generate_exercise(subject: str, difficulty: str, include_solution: bool = True) -> str:
    if include_solution:
        prompt = (
            f"Eres un profesor universitario experto. "
            f"Crea un problema original de nivel {difficulty} en la materia de {subject}. "
            f"Después de presentar el problema, proporciona también una solución detallada paso a paso. "
            f"Usa un formato claro separando 'Problema:' y 'Solución:'."
        )
    else:
        prompt = (
            f"Eres un profesor universitario experto. "
            f"Crea un problema original de nivel {difficulty} en la materia de {subject}. "
            f"NO des la solución, solo muestra el enunciado del problema."
            f"Escribe 'Problema:' al inicio."
        )
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Genera ejercicios académicos originales."},
                {"role": "user", "content": prompt}
            ],
            temperature=1.2,
            top_p=1.0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error al generar ejercicio: {str(e)}"
