from typing import Dict, Optional
import uuid
from pydantic import BaseModel

class MapalEventPayload(BaseModel):
    event_type: str
    message: Dict

class MindsmithEventPayload(BaseModel):
    type: str
    placement_id: uuid.UUID
    tenant_id: uuid.UUID
    data: Optional[Dict]
