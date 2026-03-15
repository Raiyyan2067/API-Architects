import pytest
from app.core import ubl_generator as gen

def test_invalid_xml_fails_schema_validation():
        bad_xml = "<not-ubl></not-ubl>"
        with pytest.raises(ValueError) as excinfo:
                gen.validate_xml_against_xsd(bad_xml)
        assert "UBL validation error" in str(excinfo.value)

def test_generated_xml_passes_schema_validation(monkeypatch):
        payload = {
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
                                },
                        },
                        "seller": {
                                "name": "Supplier Pty Ltd",
                                "address": {
                                        "street": "Warehouse Road 5", 
                                        "city": "Melbourne", 
                                        "postcode": "3000", 
                                        "country": "AU"
                                },
                        },
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
                        "transport_mode": "Land",
                },
                "despatch_items": [
                        {
                                "name": "Football Boots",
                                "description": "A football",
                                "unit_code": "FO",
                                "quantity": 7,
                                "seller_item_id": "SID1",
                                "buyer_item_id": "BID1",
                        }
                ],  
        }

        real_validation = gen.validate_xml_against_xsd
        monkeypatch.setattr(gen, "validate_xml_against_xsd", lambda _xml: None)
        xml = gen.generate_despatch_advice(payload)

        real_validation(xml)