# app/core/order_parser.py

from lxml import etree

# Standard UBL namespace prefixes, these are fixed by the spec
NS = {
    "cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
    "cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
}


def _text(node, path):
    """Safely run an XPath on a node and return text, or empty string."""
    results = node.xpath(path, namespaces=NS)
    if not results:
        return ""
    r = results[0]
    if hasattr(r, "text"):
        return (r.text or "").strip()
    return str(r).strip()


def _attr(node, path, attr):
    """Get an XML attribute value from the first matching element."""
    results = node.xpath(path, namespaces=NS)
    if not results:
        return ""
    return results[0].get(attr, "")


def parse_ubl_order(xml_string: str) -> dict:
    """
    Parse a UBL Order XML string and return a dict that matches
    the variable names expected by the Jinja2 despatch advice template.

    Raises ValueError if the XML is invalid or not an Order document.
    """
    try:
        root = etree.fromstring(xml_string.encode("utf-8"))
    except etree.XMLSyntaxError as e:
        raise ValueError(f"Invalid XML supplied: {e}")

    # Confirm this is actually an Order document
    local_tag = etree.QName(root.tag).localname
    if local_tag != "Order":
        raise ValueError(
            f"Expected a UBL <Order> document but received <{local_tag}>. "
            "Please upload a valid UBL Order XML file."
        )

    # ── Order header ──────────────────────────────────────────────
    data = {
        "order_id":         _text(root, "cbc:ID"),
        "sales_order_id":   _text(root, "cbc:SalesOrderID"),
        "order_uuid":       _text(root, "cbc:UUID"),
        "order_issue_date": _text(root, "cbc:IssueDate"),
        "issue_date":       _text(root, "cbc:IssueDate"),
        "order_note":       _text(root, "cbc:Note"),
        "currency_code":    _text(root, "cbc:DocumentCurrencyCode"),
    }

    if not data["order_id"]:
        raise ValueError(
            "Could not extract Order ID from the XML. Is this a valid UBL Order?")

    # ── Buyer (→ DeliveryCustomerParty in Despatch Advice) ────────
    buyer_nodes = root.xpath("cac:BuyerCustomerParty", namespaces=NS)
    buyer = buyer_nodes[0] if buyer_nodes else None

    data["buyer"] = {
        "customer_account_id":  _text(buyer, "cbc:CustomerAssignedAccountID") if buyer else "",
        "supplier_account_id":  _text(buyer, "cbc:SupplierAssignedAccountID") if buyer else "",
        "name":                 _text(buyer, "cac:Party/cac:PartyName/cbc:Name") if buyer else "",
        "street":               _text(buyer, "cac:Party/cac:PostalAddress/cbc:StreetName") if buyer else "",
        "building_name":        _text(buyer, "cac:Party/cac:PostalAddress/cbc:BuildingName") if buyer else "",
        "building_number":      _text(buyer, "cac:Party/cac:PostalAddress/cbc:BuildingNumber") if buyer else "",
        "city":                 _text(buyer, "cac:Party/cac:PostalAddress/cbc:CityName") if buyer else "",
        "postal_zone":          _text(buyer, "cac:Party/cac:PostalAddress/cbc:PostalZone") if buyer else "",
        "country_subentity":    _text(buyer, "cac:Party/cac:PostalAddress/cbc:CountrySubentity") if buyer else "",
        "address_line":         _text(buyer, "cac:Party/cac:PostalAddress/cac:AddressLine/cbc:Line") if buyer else "",
        "country_code":         _text(buyer, "cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode") if buyer else "",
        "tax_reg_name":         _text(buyer, "cac:Party/cac:PartyTaxScheme/cbc:RegistrationName") if buyer else "",
        "company_id":           _text(buyer, "cac:Party/cac:PartyTaxScheme/cbc:CompanyID") if buyer else "",
        "tax_scheme_id":        _text(buyer, "cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID") if buyer else "",
        "contact_name":         _text(buyer, "cac:Party/cac:Contact/cbc:Name") if buyer else "",
        "phone":                _text(buyer, "cac:Party/cac:Contact/cbc:Telephone") if buyer else "",
        "fax":                  _text(buyer, "cac:Party/cac:Contact/cbc:Telefax") if buyer else "",
        "email":                _text(buyer, "cac:Party/cac:Contact/cbc:ElectronicMail") if buyer else "",
    }

    # ── Seller (→ DespatchSupplierParty in Despatch Advice) ───────
    seller_nodes = root.xpath("cac:SellerSupplierParty", namespaces=NS)
    seller = seller_nodes[0] if seller_nodes else None

    data["seller"] = {
        "customer_account_id":  _text(seller, "cbc:CustomerAssignedAccountID") if seller else "",
        "name":                 _text(seller, "cac:Party/cac:PartyName/cbc:Name") if seller else "",
        "street":               _text(seller, "cac:Party/cac:PostalAddress/cbc:StreetName") if seller else "",
        "building_name":        _text(seller, "cac:Party/cac:PostalAddress/cbc:BuildingName") if seller else "",
        "building_number":      _text(seller, "cac:Party/cac:PostalAddress/cbc:BuildingNumber") if seller else "",
        "city":                 _text(seller, "cac:Party/cac:PostalAddress/cbc:CityName") if seller else "",
        "postal_zone":          _text(seller, "cac:Party/cac:PostalAddress/cbc:PostalZone") if seller else "",
        "country_subentity":    _text(seller, "cac:Party/cac:PostalAddress/cbc:CountrySubentity") if seller else "",
        "address_line":         _text(seller, "cac:Party/cac:PostalAddress/cac:AddressLine/cbc:Line") if seller else "",
        "country_code":         _text(seller, "cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode") if seller else "",
        "tax_reg_name":         _text(seller, "cac:Party/cac:PartyTaxScheme/cbc:RegistrationName") if seller else "",
        "company_id":           _text(seller, "cac:Party/cac:PartyTaxScheme/cbc:CompanyID") if seller else "",
        "tax_scheme_id":        _text(seller, "cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID") if seller else "",
        "contact_name":         _text(seller, "cac:Party/cac:Contact/cbc:Name") if seller else "",
        "phone":                _text(seller, "cac:Party/cac:Contact/cbc:Telephone") if seller else "",
        "fax":                  _text(seller, "cac:Party/cac:Contact/cbc:Telefax") if seller else "",
        "email":                _text(seller, "cac:Party/cac:Contact/cbc:ElectronicMail") if seller else "",
    }

    # ── Delivery address (from Order's <cac:Delivery>) ────────────
    delivery_nodes = root.xpath("cac:Delivery", namespaces=NS)
    delivery = delivery_nodes[0] if delivery_nodes else None

    if delivery is not None:
        data["delivery"] = {
            "street":            _text(delivery, "cac:DeliveryAddress/cbc:StreetName"),
            "building_name":     _text(delivery, "cac:DeliveryAddress/cbc:BuildingName"),
            "building_number":   _text(delivery, "cac:DeliveryAddress/cbc:BuildingNumber"),
            "city":              _text(delivery, "cac:DeliveryAddress/cbc:CityName"),
            "postal_zone":       _text(delivery, "cac:DeliveryAddress/cbc:PostalZone"),
            "country_subentity": _text(delivery, "cac:DeliveryAddress/cbc:CountrySubentity"),
            "address_line":      _text(delivery, "cac:DeliveryAddress/cac:AddressLine/cbc:Line"),
            "country_code":      _text(delivery, "cac:DeliveryAddress/cac:Country/cbc:IdentificationCode"),
            "start_date":        _text(delivery, "cac:RequestedDeliveryPeriod/cbc:StartDate"),
            "start_time":        _text(delivery, "cac:RequestedDeliveryPeriod/cbc:StartTime"),
            "end_date":          _text(delivery, "cac:RequestedDeliveryPeriod/cbc:EndDate"),
            "end_time":          _text(delivery, "cac:RequestedDeliveryPeriod/cbc:EndTime"),
        }
    else:
        # Fallback: use buyer address if no explicit Delivery element
        b = data["buyer"]
        data["delivery"] = {
            "street": b["street"], "building_name": b["building_name"],
            "building_number": b["building_number"], "city": b["city"],
            "postal_zone": b["postal_zone"], "country_subentity": b["country_subentity"],
            "address_line": b["address_line"], "country_code": b["country_code"],
            "start_date": "", "start_time": "", "end_date": "", "end_time": "",
        }

    # ── Order lines (→ DespatchLine in Despatch Advice) ───────────
    lines = []
    for order_line in root.xpath("cac:OrderLine", namespaces=NS):
        line_items = order_line.xpath("cac:LineItem", namespaces=NS)
        if not line_items:
            continue
        li = line_items[0]

        qty_nodes = li.xpath("cbc:Quantity", namespaces=NS)
        unit_code = qty_nodes[0].get("unitCode", "EA") if qty_nodes else "EA"
        quantity = (qty_nodes[0].text or "0").strip() if qty_nodes else "0"

        lines.append({
            "id":             _text(li, "cbc:ID"),
            "sales_order_id": _text(li, "cbc:SalesOrderID"),
            "quantity":       quantity,
            "unit_code":      unit_code,
            "description":    _text(li, "cac:Item/cbc:Description"),
            "name":           _text(li, "cac:Item/cbc:Name"),
            "buyers_id":      _text(li, "cac:Item/cac:BuyersItemIdentification/cbc:ID"),
            "sellers_id":     _text(li, "cac:Item/cac:SellersItemIdentification/cbc:ID"),
        })

    data["order_lines"] = lines
    return data
