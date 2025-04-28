# app/agents/corrector_agent.py

from app.agents.agent_manager import AgentManager

class CorrectorAgent:
    def __init__(self):
        self.manager = AgentManager()
        self.plugin_name = "text_corrector"

    async def corregir_texto(self, texto: str):
        response = await self.manager.run_plugin(self.plugin_name, texto=texto)
        return response
