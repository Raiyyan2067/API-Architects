import pytest
from app.core.ubl_generator import generate_despatch_advice
from app.models.despatch_models import DespatchRequest, Shipment, OrderInfo, Party, PartyAddress, LineItem, DeliveryAddress


def valid_request():
    return DespatchRequest(
        despatch_id="D100",
        issue_date="2025-03-10",
        issue_time="10:00:00",
        order=OrderInfo(
            order_id="ORDER123",
            buyer=Party(name="Buyer", address=PartyAddress(
                street="s", city="c", postcode="p", country="AU")),
            seller=Party(name="Seller", address=PartyAddress(
                street="s", city="c", postcode="p", country="AU"))
        ),
        shipment=Shipment(
            shipment_id="S1",
            handling_code="Normal",
            information="Standard handling",
            delivery_address=DeliveryAddress(
                street="s", city="c", postcode="p", country="AU"),
            transport_unit_id="T1",
            transport_mode="Land"
        ),
        despatch_items=[
            LineItem(
                name="Widget",
                description="A widget",
                unit_code="EA",
                quantity=3,
                seller_item_id="SID1",
                buyer_item_id="BID1"
            )
        ]
    )


def test_success():
    req = valid_request()
    xml = generate_despatch_advice(req)
    assert "<DespatchAdvice" in xml


def test_missing_required_field():
    req = valid_request()
    req.despatch_id = None
    with pytest.raises(Exception):
        generate_despatch_advice(req)


def test_invalid_date():
    with pytest.raises(Exception):
        DespatchRequest(
            despatch_id="D",
            issue_date="2025",
            issue_time="10:00:00",
            order=valid_request().order,
            shipment=valid_request().shipment,
            despatch_items=valid_request().despatch_items
        )
