from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, func
from enums import DeviceType, Status
from datetime import datetime
import uuid

class Base(DeclarativeBase):
    pass

class Device(Base):
    __tablename__ = "devices"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str]
    serial: Mapped[str] = mapped_column(unique=True, index=True)
    device_type: Mapped[DeviceType]
    rack: Mapped[str]
    status: Mapped[Status] = mapped_column(default=Status.PLANNED)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    interfaces: Mapped[list["Interface"]] = relationship(back_populates="device")

class Interface(Base):
    __tablename__ = "interfaces"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4) # autopopulate id with uuid4, pk
    device_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("devices.id"), index=True)
    device: Mapped["Device"] = relationship(back_populates="interfaces")
    name: Mapped[str]
    mac: Mapped[str]
    vlan_id: Mapped[int | None]

