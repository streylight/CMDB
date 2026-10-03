from enum import StrEnum

class DeviceType(StrEnum):
    SERVER = "server"
    SWITCH = "switch"
    PDU = "pdu"
    STORAGE = "storage"

class Status(StrEnum):
    PLANNED = "planned"
    PROVISIONING = "provisioning"
    ACTIVE = "active"
    MAINTENANCE = "maintenance"
    DECOMMISSIONED = "decommissioned"