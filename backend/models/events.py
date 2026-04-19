from pydantic import BaseModel
from typing import Any, Optional

class SSEEvent(BaseModel):
    event_type: str
    data: Any
    id: Optional[int] = None
