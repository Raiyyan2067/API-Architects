import pytest
from unittest.mock import patch
from app.core.ubl_generator import generate_despatch_advice
from app.models.despatch_models import DespatchRequest, Shipment, OrderInfo, Party, PartyAddress, LineItem, DeliveryAddress


def valid_request():
    """Returns fully valid DespatchRequest"""
    return DespatchRequest(
        despatch_id="D100",
        issue_date="2025-03-10",
        issue_time="10:00:00",
        order=OrderInfo(
            order_id="ORDER-001",
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
                quantity=3.5,
                seller_item_id="SID1",
                buyer_item_id="BID1"
            )
        ]
    )


@patch("app.core.ubl_generator.get_order")
def test_generate_xml_success(mock_get_order):
    """Tests that a valid request produces valid XML content."""
    # Mock the database to return a dummy order so the test doesn't need the JSON file
    mock_get_order.return_value = {"order_id": "ORDER-001"}

    req = valid_request()
    xml = generate_despatch_advice(req)

    # Assertions: Check for specific UBL elements
    assert "<DespatchAdvice" in xml
    assert "<cbc:ID>D100</cbc:ID>" in xml
    assert "DeliveredQuantity" in xml
    assert "3.5" in xml
    assert "<cbc:Name>Widget</cbc:Name>" in xml


@patch("app.core.ubl_generator.get_order")
def test_order_not_found_error(mock_get_order):
    """Tests that the generator raises an error if the Order ID doesn't exist."""
    mock_get_order.return_value = None  # Simulate order not found

    req = valid_request()
    with pytest.raises(ValueError, match="Order does not exist"):
        generate_despatch_advice(req)


def test_pydantic_validation_invalid_date():
    """Tests that Pydantic catches bad date formats before generation starts."""
    with pytest.raises(Exception):
        # Invalid date format (missing DD)
        DespatchRequest(
            despatch_id="D",
            issue_date="2025-03",
            issue_time="10:00:00",
            order=valid_request().order,
            shipment=valid_request().shipment,
            despatch_items=valid_request().despatch_items
        )


def test_pydantic_validation_negative_quantity():
    """Tests that Pydantic prevents shipping negative amounts."""
    req_data = valid_request().model_dump()
    req_data['despatch_items'][0]['quantity'] = -5.0  # Illegal quantity

    with pytest.raises(Exception):
        DespatchRequest(**req_data)


@patch("app.core.ubl_generator.get_order")
def test_missing_top_level_field(mock_get_order):
    """Tests generator-level validation for missing mandatory fields."""
    mock_get_order.return_value = {"order_id": "ORDER-001"}

    req = valid_request()
    # Pydantic might catch this, but we test the generator's safety check too
    req_dict = req.model_dump()
    req_dict['shipment'] = None

    with pytest.raises(ValueError, match="Missing required field: shipment"):
        generate_despatch_advice(req_dict)


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
