from pydantic import BaseModel, ConfigDict
from datetime import datetime
from enums import DeviceType, Status
import uuid

## Schemas
class BaseDevice(BaseModel):
    name: str
    serial: str
    device_type: DeviceType
    rack: str

class DeviceResponse(BaseDevice):
    model_config = ConfigDict(from_attributes=True) ## lets Pydantic read attributes from ORM objects
    id: uuid.UUID
    status: Status # default to planned
    created_at: datetime
    updated_at: datetime

class DeviceCreate(BaseDevice):
    pass

class DeviceUpdate(BaseModel):
    name: str | None = None
    rack: str | None = None
    status: Status | None = None

class Interface(BaseModel):
    id: uuid.UUID
    device_id: uuid.UUID
    name: str
    mac: str
    vlan_id: int | None = None