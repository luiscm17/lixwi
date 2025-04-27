from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from app.agents.agent_manager import AgentManager

router = APIRouter()
agent_manager = AgentManager()

# Esquema de entrada
class AgentRequest(BaseModel):
    plugin_name: str
    input_variables: Dict[str, Any]

# Esquema de respuesta
class AgentResponse(BaseModel):
    result: str

# Endpoint para ejecutar un plugin
@router.post("/execute", response_model=AgentResponse, summary="Ejecutar un plugin IA", tags=["Agent"])
async def execute_agent(request: AgentRequest):
    try:
        response = await agent_manager.run_plugin(
            plugin_name=request.plugin_name,
            **request.input_variables
        )
        return AgentResponse(result=response)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error ejecutando plugin: {str(e)}")
