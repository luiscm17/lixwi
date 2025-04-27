# app/core/memory.py

from typing import Dict, List

# Almacenamiento en memoria de mensajes por sesión
_sessions: Dict[str, List[dict]] = {}

def get_session_history(session_id: str) -> List[dict]:
    return _sessions.get(session_id, [])

def add_message_to_session(session_id: str, role: str, content: str) -> None:
    if session_id not in _sessions:
        _sessions[session_id] = []
    _sessions[session_id].append({"role": role, "content": content})

def clear_session(session_id: str) -> None:
    if session_id in _sessions:
        del _sessions[session_id]
