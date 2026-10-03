from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from enums import DeviceType, Status
import uuid

## Models
class BaseDevice(BaseModel):
    name: str
    serial: str
    device_type: DeviceType
    rack: str

class Device(BaseDevice):
    id: uuid.UUID
    status: Status = Status.PLANNED # default to planned
    created_at: datetime
    updated_at: datetime

class DeviceCreate(BaseDevice):
    pass

class Interface(BaseModel):
    id: uuid.UUID
    device_id: uuid.UUID
    name: str
    mac: str
    vlan_id: int | None = None

app = FastAPI()

device_database = {
    uuid.UUID("a1b2c3d4-0001-4e9a-8f3b-111111111111"): Device(
        id=uuid.UUID("a1b2c3d4-0001-4e9a-8f3b-111111111111"),
        status=Status.ACTIVE,
        created_at=datetime(2026, 1, 10, 9, 30, 0),
        updated_at=datetime(2026, 1, 12, 14, 0, 0),
        name="web-srv-01",
        serial="SN-SRV-00123",
        device_type=DeviceType.SERVER,
        rack="R-14",
    ),
    uuid.UUID("a1b2c3d4-0002-4e9a-8f3b-222222222222"): Device(
        id=uuid.UUID("a1b2c3d4-0002-4e9a-8f3b-222222222222"),
        status=Status.PROVISIONING,
        created_at=datetime(2026, 2, 1, 11, 0, 0),
        updated_at=datetime(2026, 2, 1, 11, 0, 0),
        name="core-sw-02",
        serial="SN-SWX-00456",
        device_type=DeviceType.SWITCH,
        rack="R-02",
    ),
}

@app.get("/")
async def root():
    return { "message": "goodbye world!"}

@app.get("/devices/{device_id}", response_model=Device)
async def get_device_by_id(device_id: uuid.UUID) -> Device:
    if device_id in device_database:
        return device_database[device_id]
    else:
        raise HTTPException(status_code=404, detail="Device not found!!")

@app.post("/devices/")
async def create_device(device: DeviceCreate):
    ts = datetime.now()
    new_device = Device(**device.model_dump(), id=uuid.uuid4(),created_at = ts, updated_at = ts)
    device_database[new_device.id] = new_device
    return { "message:": "device created successfully!", "device:": device }


