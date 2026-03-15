from pydantic import BaseModel, Field, validator
from typing import List


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
    quantity: int
    seller_item_id: str
    buyer_item_id: str


class DespatchRequest(BaseModel):
    despatch_id: str
    issue_date: str
    issue_time: str
    order: OrderInfo
    shipment: Shipment
    despatch_items: List[LineItem]

    @validator("issue_date")
    def date_format(cls, v):
        if len(v.split("-")) != 3:
            raise ValueError("issue_date must be YYYY-MM-DD")
        return v

    @validator("issue_time")
    def time_format(cls, v):
        if ":" not in v:
            raise ValueError("issue_time must be HH:MM:SS")
        return v
