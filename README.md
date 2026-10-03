# CMDB

A small configuration management database with a REST API. It tracks
devices (servers, switches, PDUs, storage) and their network interfaces,
stored in Postgres.

> [!NOTE]
> Scope is kept small on purpose: two tables, seven endpoints.

## Stack

- Python 3.13, managed with uv
- FastAPI (async)
- Pydantic v2 for request/response validation
- SQLAlchemy 2.0 (async) with asyncpg
- PostgreSQL 17
- Alembic for migrations

## Data model

A device has one-to-many interfaces. An interface only belongs to a single device.

**Device**: name, serial (unique), type, rack, status, created/updated timestamps

**Interface**: name, MAC address, VLAN (optional, 1-4094)

Status follows the device lifecycle:

    planned -> provisioning -> active -> maintenance -> decommissioned

Devices are never deleted, only marked `decommissioned`, so the history
stays in the database.

## API

    POST   /devices
    GET    /devices                  cursor pagination
    GET    /devices/{id}
    PATCH  /devices/{id}
    POST   /devices/{id}/interfaces
    GET    /devices/{id}/interfaces
    PATCH  /interfaces/{id}          e.g. move an interface to another VLAN

IDs, timestamps and the initial status are set by the server. Clients
can't set them.

## Running it locally

Needs Postgres running locally with a database named `cmdb`.

    createdb cmdb
    uv sync
    uv run alembic upgrade head
    uv run fastapi dev main.py

Interactive API docs at http://localhost:8000/docs.

## Status

Work in progress. Models are done; the endpoints are still being moved
from an in-memory store onto the database.
