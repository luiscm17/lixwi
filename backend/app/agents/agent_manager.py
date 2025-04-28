from app.plugins.plugins_loader import load_plugins
from app.services.llm_service import get_ai_response

class AgentManager:
    def __init__(self):
        self.plugins = load_plugins()

    def list_plugins(self):
        """Listar todos los plugins disponibles"""
        return list(self.plugins.keys())

    def get_plugin(self, plugin_name: str):
        """Obtener un plugin específico"""
        return self.plugins.get(plugin_name)

    async def run_plugin(self, plugin_name: str, **kwargs):
        """Usar un plugin para generar una respuesta"""
        plugin = self.get_plugin(plugin_name)
        if not plugin:
            return f"Plugin '{plugin_name}' no encontrado."

        # Reemplazar variables en el prompt
        prompt_filled = plugin.prompt
        for var in plugin.input_variables:
            if var not in kwargs:
                return f"Falta la variable requerida: {var}"
            prompt_filled = prompt_filled.replace(f"{{{{{var}}}}}", str(kwargs[var]))

        # Llamar al LLM pasando el prompt y las execution_settings
        response = await get_ai_response(
            prompt=prompt_filled,
            execution_settings=plugin.execution_settings
        )
        return response
