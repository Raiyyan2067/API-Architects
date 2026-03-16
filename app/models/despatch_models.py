from pydantic import BaseModel, Field, field_validator
from typing import List, Optional


class PartyAddress(BaseModel):
    street: str
    city: str
    postcode: str
    country: str


class Party(BaseModel):
    name: str
    address: PartyAddress


class OrderInfo(BaseModel):
    order_id: str
    buyer: Party
    seller: Party
    sales_order_id: str | None = None


class DeliveryAddress(BaseModel):
    street: str
    city: str
    postcode: str
    country: str


class Shipment(BaseModel):
    shipment_id: str
    handling_code: str
    information: str
    delivery_address: DeliveryAddress
    transport_unit_id: str
    transport_mode: str


class LineItem(BaseModel):
    name: str
    description: str
    unit_code: str
    quantity: float = Field(gt=0)
    seller_item_id: str
    buyer_item_id: Optional[str] = None


class DespatchRequest(BaseModel):
    despatch_id: str
    issue_date: str
    issue_time: str
    order: OrderInfo
    shipment: Shipment
    despatch_items: List[LineItem]

    @field_validator("issue_date")
    @classmethod
    def validate_date(cls, v):
        if len(v) != 10 or v[4] != "-" or v[7] != "-":
            raise ValueError("Date must be YYYY-MM-DD")
        return v

    @field_validator("issue_time")
    @classmethod
    def time_format(cls, v):
        if ":" not in v:
            raise ValueError("issue_time must be HH:MM:SS")
        return v
