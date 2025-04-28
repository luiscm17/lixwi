# app/core/semantic_kernel.py

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion
from app.core.config import settings

# Crear una instancia global del Kernel
kernel = Kernel()

# Configurar el servicio de AI que se va a usar
api_key = settings.OPENAI_API_KEY  # o tu proveedor
deployment_name = settings.OPENAI_DEPLOYMENT_NAME  # opcional, si usas Azure
model_name = settings.OPENAI_MODEL_NAME

# Conector básico para OpenAI
kernel.add_text_completion_service(
    "openai-gpt",
    OpenAITextCompletion(
        service_id="openai-gpt",
        api_key=api_key,
        model=model_name,
    )
)
