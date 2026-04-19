from pydantic import BaseModel
from typing import Any, Dict, List, Optional

class AgentInput(BaseModel):
    query: str
    context: Optional[Dict[str, Any]] = None

class AgentOutput(BaseModel):
    agent_name: str
    status: str
    data: Any
    confidence: float
    reasoning: str
