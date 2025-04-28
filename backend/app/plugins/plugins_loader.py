import os
import json
from pathlib import Path
from typing import Dict, Optional

class Plugin:
    def __init__(self, name: str, description: str, input_variables: list, output_variable: Optional[str], prompt: str, execution_settings: dict):
        self.name = name
        self.description = description
        self.input_variables = input_variables
        self.output_variable = output_variable
        self.prompt = prompt
        self.execution_settings = execution_settings

    def __repr__(self):
        return f"<Plugin name={self.name}>"

def load_plugins(plugins_dir: str = "app/plugins") -> Dict[str, Plugin]:
    plugins = {}

    # Escanear subcarpetas
    for plugin_folder in os.listdir(plugins_dir):
        folder_path = os.path.join(plugins_dir, plugin_folder)
        if os.path.isdir(folder_path):
            config_path = os.path.join(folder_path, "config.json")
            prompt_path = os.path.join(folder_path, "skprompt.txt")

            # Verificar que existan los archivos necesarios
            if os.path.isfile(config_path) and os.path.isfile(prompt_path):
                try:
                    # Cargar configuración del JSON
                    with open(config_path, "r", encoding="utf-8") as f:
                        config_data = json.load(f)

                    # Cargar prompt
                    with open(prompt_path, "r", encoding="utf-8") as f:
                        prompt_text = f.read()

                    # Extraer posibles campos del config
                    description = config_data.get("description", "Sin descripción")
                    execution_settings = config_data.get("execution_settings", {})
                    input_variables = extract_input_variables(prompt_text)
                    
                    # Crear plugin
                    plugin = Plugin(
                        name=plugin_folder,  # El nombre será el mismo de la carpeta
                        description=description,
                        input_variables=input_variables,
                        output_variable=None,  # (lo dejamos nulo si no está especificado)
                        prompt=prompt_text,
                        execution_settings=execution_settings
                    )

                    plugins[plugin.name] = plugin

                except Exception as e:
                    print(f"Error cargando plugin {plugin_folder}: {str(e)}")

    return plugins

def extract_input_variables(prompt: str) -> list:
    """Detectar automáticamente las variables entre llaves en el prompt."""
    import re
    return re.findall(r"\{\{(\w+)\}\}", prompt)
