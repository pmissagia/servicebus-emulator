from typing import Dict
from pydantic import BaseModel

class MapalEventPayload(BaseModel):
    event_type: str
    message: Dict

class MindsmithEventPayload(BaseModel):
    event_type: str
    message: Dict
