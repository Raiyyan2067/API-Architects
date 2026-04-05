from jinja2 import Environment, FileSystemLoader
import os
import json
from datetime import date
import uuid
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


def generate_despatch_advice(order_data: dict, carrier: str = "", dispatch_date: str = "", notes: str = "") -> str:
    """
    Generate a UBL Despatch Advice XML from order_data dict
    (produced by order_parser.parse_ubl_order).
    """
    today = dispatch_date if dispatch_date else str(date.today())
    despatch_id = str(uuid.uuid4().int)[:6]
    despatch_uuid = str(uuid.uuid4()).upper()

    # Merge generated fields into the data dict for the template
    context = {
        **order_data,
        "despatch_id":   despatch_id,
        "despatch_uuid": despatch_uuid,
        "issue_date":    today,
        "carrier":       carrier,
        "notes":         notes,
    }

    # Load template and render XML
    template = env.get_template("despatch_advice_template.xml")
    xml = template.render(**context)

    # Validate XML using UBL XSD
    validate_xml_against_xsd(xml)

    return xml
