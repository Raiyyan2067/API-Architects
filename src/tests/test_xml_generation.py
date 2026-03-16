import pytest
from app.core import ubl_generator as gen

def _valid_payload():
    return {
        "despatch_id": "D123",
        "issue_date": "2025-03-10",
        "issue_time": "10:00:00",
        "order": {
            "order_id": "ORDER123",
            "sales_order_id": "SO-99887",
            "buyer": {
                "name": "Football Club Buyer Ltd",
                "address": {
                    "street": "Buyer Street 12", 
                    "city": "Sydney", 
                    "postcode": "2000", 
                    "country": "AU"
                }
            },
            "seller": {
                "name": "Supplier Pty Ltd",
                "address": {
                    "street": "Warehouse Road 5", 
                    "city": "Melbourne", 
                    "postcode": "3000", 
                    "country": "AU"
                }
            }
        },
        "shipment": {
            "shipment_id": "SHIP1",
            "handling_code": "Normal",
            "information": "Standard handling",
            "delivery_address": {
                "street": "1 Road", 
                "city": "Sydney", 
                "postcode": "2000", 
                "country": "AU"
            },
            "transport_unit_id": "TU1",
            "transport_mode": "Land"
        },
        "despatch_items": [
            {
                "name": "Football Boots",
                "description": "A football",
                "unit_code": "FO",
                "quantity": 7,
                "seller_item_id": "SID1",
                "buyer_item_id": "BID1"
            }
        ]
    }

def test_generate_despatch_advice_renders_in_xml(monkeypatch):
    """Test XML rendering"""

    monkeypatch.setattr(gen, "validate_xml_against_xsd", lambda _xml: None)
    monkeypatch.setattr(gen, "get_order", lambda order_id: {"order_id": order_id})

    xml = gen.generate_despatch_advice(_valid_payload())

    assert "<DespatchAdvice" in xml
    assert "<cbc:ID>D123</cbc:ID>" in xml
    assert "Football Club Buyer Ltd" in xml
    assert "Supplier Pty Ltd" in xml

def test_missing_required_field_raises(monkeypatch):
    """Test that missing required fields raise ValueError"""
    monkeypatch.setattr(gen, "validate_xml_against_xsd", lambda _xml: None)
    monkeypatch.setattr(gen, "get_order", lambda order_id: {"order_id": order_id})

    payload = _valid_payload()
    payload["despatch_id"] = ""
    with pytest.raises(ValueError) as excinfo:
        gen.generate_despatch_advice(payload)

    assert "Missing required field: despatch_id" in str(excinfo.value)