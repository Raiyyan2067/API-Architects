from xmlschema import XMLSchema, XMLSchemaException
from app.core.config import XSD_PATH

schema = XMLSchema(XSD_PATH)


def validate_xml_against_xsd(xml_content: str):
    try:
        schema.validate(xml_content)
    except XMLSchemaException as e:
        raise ValueError(f"UBL validation error: {e}")
