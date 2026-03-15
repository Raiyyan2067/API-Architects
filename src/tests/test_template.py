from src.main.ubl_generator import generate_despatch_advice


def test_generate_minimal_xml():
    data = {
        "despatch_id": "D123",
        "issue_date": "2025-03-10",
        "order": {
            "order_id": "ORDER123",
            "seller": {"name": "Test Seller"},
            "buyer": {"name": "Test Buyer"}
        },
        "shipment": {"shipment_id": "SHIP1"},
        "despatch_items": [
            {"name": "Widget A", "unit_code": "EA", "quantity": 3}
        ]
    }

    xml = generate_despatch_advice(data)
    assert "<cbc:ID>D123</cbc:ID>" in xml
    assert "<cbc:Name>Test Buyer</cbc:Name>" in xml
