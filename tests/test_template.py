from app.core import ubl_generator as gen

def test_generate_minimal_xml(monkeypatch):
    """Test minimal payload renders correctly in XML"""

    monkeypatch.setattr(gen, "get_order", lambda order_id: {"order_id": order_id})
    monkeypatch.setattr(gen, "validate_xml_against_xsd", lambda _xml: None)

    data = {
        "despatch_id": "D123",
        "issue_date": "2025-03-10",
        "order": {
            "order_id": "ORDER-001",
            "seller": {"name": "Test Seller"},
            "buyer": {"name": "Test Buyer"}
        },
        "shipment": {"shipment_id": "SHIP1"},
        "despatch_items": [
            {"name": "Widget A", "unit_code": "EA", "quantity": 3}
        ]
    }

    xml = gen.generate_despatch_advice(data)

    assert "<cbc:ID>D123</cbc:ID>" in xml
    assert "<cbc:Name>Test Buyer</cbc:Name>" in xml
    assert "<cbc:Name>Test Seller</cbc:Name>" in xml