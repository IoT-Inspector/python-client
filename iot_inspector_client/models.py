"""Define models."""

import datetime as dt
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Tenant(BaseModel):
    """Tenant Model."""

    id: UUID
    name: str


class FirmwareMetadata(BaseModel):
    """Firmware metadata model."""

    name: str
    version: Optional[str] = None
    release_date: Optional[dt.datetime] = None
    notes: Optional[str] = None
    vendor_name: str
    product_name: str
    product_category: Optional[str] = None
    product_group_id: UUID
