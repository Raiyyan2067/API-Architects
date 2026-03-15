import os
from jinja2 import Environment, FileSystemLoader
from xmlschema import XMLSchema, XMLSchemaException
from datetime import datetime


APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = os.path.join(APP_DIR, "templates")
XSD_PATH = os.path.join(APP_DIR, "xsd", "maindoc",
                        "UBL-DespatchAdvice-2.1.xsd")

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
schema = XMLSchema(XSD_PATH)


def validate_xml_against_xsd(xml_content: str):
    try:
        schema.validate(xml_content)
    except XMLSchemaException as e:
        raise ValueError(f"UBL validation error: {e}")


def generate_despatch_advice(request_model):
    if hasattr(request_model, "model_dump"):
        merged_data = request_model.model_dump()
    elif hasattr(request_model, "dict"):
        merged_data = request_model.dict()
    else:
        merged_data = request_model

    required_fields = ["despatch_id", "issue_date", "order", "shipment"]
    for field in required_fields:
        if merged_data.get(field) in (None, "", [], {}):
            raise ValueError(f"Missing required field: {field}")

    merged_data["order_details"] = merged_data["order"]
    template = env.get_template("despatch_advice_template.xml")
    xml = template.render(**merged_data)
    validate_xml_against_xsd(xml)
    return xml


def parse_filename(filename):
    parts = filename.replace(".xml", "").split("_")
    despatch_id = parts[1]
    doc_uuid = parts[2]
    timestamp_str = parts[3]
    try:
        date = datetime.strptime(timestamp_str, "%Y-%m-%dT-%H%M%S")
        iso_timestamp = date.strftime("%Y-%m-%dT%H:%M:%S")
    except ValueError:
        iso_timestamp = timestamp_str

    return {
        "despatch_id": despatch_id,
        "uuid": doc_uuid,
        "timestamp": iso_timestamp,
        "filename": filename,
        "download_url": f"/ubl/v2/despatch-advice/download/{doc_uuid}"
    }
