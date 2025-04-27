import os
import json
from pathlib import Path
from typing import Dict

class Plugin:
    def __init__(self, name: str, description: str, input_variables: list, output_variable: str, prompt: str):
        self.name = name
        self.description = description
        self.input_variables = input_variables
        self.output_variable = output_variable
        self.prompt = prompt

    def __repr__(self):
        return f"<Plugin name={self.name}>"

def load_plugins(plugins_dir: str = "app/plugins") -> Dict[str, Plugin]:
    plugins = {}

    # Escanear subcarpetas
    for plugin_folder in os.listdir(plugins_dir):
        folder_path = os.path.join(plugins_dir, plugin_folder)
        if os.path.isdir(folder_path):
            skprompt_path = os.path.join(folder_path, "skprompt.json")
            prompt_path = os.path.join(folder_path, "prompt.txt")

            # Verificar que existan los archivos necesarios
            if os.path.isfile(skprompt_path) and os.path.isfile(prompt_path):
                try:
                    # Cargar metadata del JSON
                    with open(skprompt_path, "r", encoding="utf-8") as f:
                        skprompt_data = json.load(f)

                    # Cargar prompt
                    with open(prompt_path, "r", encoding="utf-8") as f:
                        prompt_text = f.read()

                    plugin = Plugin(
                        name=skprompt_data["name"],
                        description=skprompt_data["description"],
                        input_variables=skprompt_data.get("input_variables", []),
                        output_variable=skprompt_data.get("output_variable", ""),
                        prompt=prompt_text
                    )

                    plugins[plugin.name] = plugin

                except Exception as e:
                    print(f"Error cargando plugin {plugin_folder}: {str(e)}")
    return plugins
