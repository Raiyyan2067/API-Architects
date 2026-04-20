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


def generate_despatch_advice(
    order_data: dict,
    carrier: str = "",
    dispatch_date: str = "",
    notes: str = "",
    partial_lines: dict = None,   # optional: {line_id: dispatched_qty}
) -> str:
    """
    Generate a UBL Despatch Advice XML from order_data dict
    (produced by order_parser.parse_ubl_order).

    partial_lines: dict keyed by line id → dispatched quantity (float/str).
    If a line id is not in partial_lines, its full ordered quantity is used.
    Backorder quantity is auto-calculated when dispatched < ordered.
    """
    today = dispatch_date if dispatch_date else str(date.today())
    despatch_id = str(uuid.uuid4().int)[:6]
    despatch_uuid = str(uuid.uuid4()).upper()

    # Apply partial quantities to order lines
    enriched_lines = []
    for line in order_data.get("order_lines", []):
        ordered_qty = float(line["quantity"]) if line["quantity"] else 0.0
        if partial_lines and line["id"] in partial_lines:
            dispatched_qty = float(partial_lines[line["id"]])
            # Guard: dispatched cannot exceed ordered
            dispatched_qty = min(dispatched_qty, ordered_qty)
            dispatched_qty = max(dispatched_qty, 0.0)
        else:
            dispatched_qty = ordered_qty

        backorder_qty = ordered_qty - dispatched_qty

        enriched_lines.append({
            **line,
            "delivered_qty":  int(dispatched_qty) if dispatched_qty == int(dispatched_qty) else dispatched_qty,
            "backorder_qty":  int(backorder_qty)  if backorder_qty  == int(backorder_qty)  else backorder_qty,
        })

    # Merge generated fields into the data dict for the template
    # order_issue_date = the date from the original Order XML (not the dispatch date)
    # issue_date       = the dispatch date (today or user-provided)
    context = {
        **order_data,
        "order_lines":      enriched_lines,
        "despatch_id":      despatch_id,
        "despatch_uuid":    despatch_uuid,
        "issue_date":       today,
        "order_issue_date": order_data.get("order_issue_date", ""),
        "currency_code":    order_data.get("currency_code", ""),
        "carrier":          carrier,
        "notes":            notes,
    }

    # Load template and render XML
    template = env.get_template("despatch_advice_template.xml")
    xml = template.render(**context)

    # Validate XML using UBL XSD
    validate_xml_against_xsd(xml)

    return xml
