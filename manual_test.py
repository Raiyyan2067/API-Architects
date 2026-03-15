from app.models.despatch_models import (
    DespatchRequest, Shipment, OrderInfo, Party, PartyAddress,
    LineItem, DeliveryAddress
)
from app.core.ubl_generator import generate_despatch_advice

# prepare a request payload
req = DespatchRequest(
    despatch_id="DTEST01",
    issue_date="2025-03-10",
    issue_time="09:00:00",

    order=OrderInfo(
        order_id="ORDER123",
        buyer=Party(
            name="Buyer Test",
            address=PartyAddress(
                street="Street 1", city="City", postcode="2000", country="AU")
        ),
        seller=Party(
            name="Seller Test",
            address=PartyAddress(
                street="Street 2", city="City", postcode="3000", country="AU")
        )
    ),

    shipment=Shipment(
        shipment_id="SHIP1",
        handling_code="Normal",
        information="Handled carefully",
        delivery_address=DeliveryAddress(
            street="Del St", city="Del City", postcode="4000", country="AU"),
        transport_unit_id="TU001",
        transport_mode="Land"
    ),

    despatch_items=[
        LineItem(
            name="Item A",
            description="Sample item",
            unit_code="EA",
            quantity=5,
            seller_item_id="SID-1",
            buyer_item_id="BID-1"
        )
    ]
)

xml_output = generate_despatch_advice(req)

# show the XML result
print("\nGenerated XML:\n")
print(xml_output)

# save to file
with open("output_despatch.xml", "w", encoding="utf-8") as f:
    f.write(xml_output)

print("\nSaved to output_despatch.xml")
