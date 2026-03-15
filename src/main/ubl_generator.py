from jinja2 import Environment, FileSystemLoader
import os
import json
from xmlschema import XMLSchema, XMLSchemaException

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
XSD_PATH = os.path.join(BASE_DIR, "xsd", "maindoc",
                        "UBL-DespatchAdvice-2.1.xsd")

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


def get_order(order_id: str):
    data_path = os.path.join(BASE_DIR, "data", "mock_orders.json")
    with open(data_path) as f:
        data = json.load(f)
    return data.get(order_id)


def validate_xml_against_xsd(xml_content: str):
    schema = XMLSchema(XSD_PATH)
    try:
        schema.validate(xml_content)
    except XMLSchemaException as e:
        raise ValueError(f"UBL validation error: {e}")


def generate_despatch_advice(request_model):

    # Support both Pydantic models and plain dicts
    if hasattr(request_model, "model_dump"):
        merged_data = request_model.model_dump()
    elif hasattr(request_model, "dict"):
        merged_data = request_model.dict()
    else:
        merged_data = request_model

    # Validate required top-level fields
    required_fields = ["despatch_id", "issue_date", "order", "shipment"]
    for field in required_fields:
        if merged_data.get(field) in (None, "", [], {}):
            raise ValueError(f"Missing required field: {field}")

    # Extract order_id safely from merged_data
    order_id = merged_data["order"].get("order_id")
    order_details = get_order(order_id)

    if not order_details:
        raise ValueError("Order does not exist")

    # Load template and render XML
    template = env.get_template("despatch_advice_template.xml")
    xml = template.render(merged_data)

    # Validate XML using UBL XSD
    validate_xml_against_xsd(xml)

    return xml
