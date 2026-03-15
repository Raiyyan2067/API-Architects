from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def _valid_request_json():
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

def test_health_check():
        res = client.get("/ubl/v2/despatch-advice/health")
        assert res.status_code == 200
        assert res.json() == {"status": "ok"}

def test_generate_endpoint_returns_xml_file():
        res = client.post("/ubl/v2/despatch-advice/generate", json=_valid_request_json())
        assert res.status_code == 201

        assert res.headers["content-type"].startswith("application/xml")

        assert "despatch-uuid" in {k.lower(): v for k, v in res.headers.items()}
        assert "despatch-id" in {k.lower(): v for k, v in res.headers.items()}

        body = res.text
        assert "<DespatchAdvice" in body
        assert "D123" in body


def test_list_endpoint_after_generation():
        res = client.post("/ubl/v2/despatch-advice/generate", json=_valid_request_json())
        assert res.status_code == 201

        res = client.get("/ubl/v2/despatch-advice/list")
        assert res.status_code == 200

        data = res.json()
        assert "files" in data
        assert isinstance(data["files"], list)
        assert len(data["files"]) >= 1

def test_generate_invalid_request_returns_422():
        bad = _valid_request_json()
        bad["issue_date"] = "2025"
        res = client.post("/ubl/v2/despatch-advice/generate", json=bad)
        assert res.status_code == 422
