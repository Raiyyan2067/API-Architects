import os
from app.data.mock_db import get_order
from app.models.despatch_models import (
    DespatchRequest, Shipment, OrderInfo, Party, PartyAddress,
    LineItem, DeliveryAddress
)
from app.core.ubl_generator import generate_despatch_advice


def run_manual_test(target_order_id: str):
    print(f"--- Starting Manual Test for {target_order_id} ---")

    # 1. Fetch data from your Mock DB (Ticket B-03)
    order_data = get_order(target_order_id)

    if not order_data:
        print(f"Error: Order {target_order_id} not found in mock_orders.json")
        return

    # 2. Map the JSON data to your Pydantic Models (Ticket B-04)

    items_to_ship = []
    for item in order_data['items']:
        items_to_ship.append(
            LineItem(
                name=item['name'],
                description=item['description'],
                unit_code=item['unit_code'],
                quantity=item['quantity'],
                seller_item_id=item['sku'],
                # Use .get() to avoid "Field Required" errors if it's missing in JSON
                buyer_item_id=item.get('buyer_item_id')
            )
        )

    # 3. Create the full Request Payload
    req = DespatchRequest(
        despatch_id="DESP-2025-001",
        issue_date="2025-03-17",
        issue_time="14:30:00",

        order=OrderInfo(
            order_id=order_data['order_id'],
            order_uuid=order_data.get('order_uuid', 'N/A'),
            buyer=Party(
                name=order_data['buyer_name'],
                address=PartyAddress(
                    street="123 Buyer Lane", city="Sydney", postcode="2000", country="AU")
            ),
            seller=Party(
                name=order_data['seller_name'],
                address=PartyAddress(
                    street="5 Warehouse Rd", city="Melbourne", postcode="3000", country="AU")
            )
        ),

        shipment=Shipment(
            shipment_id="SHIP-777",
            handling_code="Standard",
            information="Fragile - Handle with care",
            delivery_address=DeliveryAddress(
                street="456 Delivery St", city="Brisbane", postcode="4000", country="AU"
            ),
            transport_unit_id="TRUCK-01",
            transport_mode="Road"
        ),

        despatch_items=items_to_ship
    )

    # 4. Generate the XML (Ticket B-02)
    try:
        xml_output = generate_despatch_advice(req)

        # Print a snippet to console
        print("\nGenerated XML (First 500 chars):")
        print(xml_output[:500] + "...")

        # 5. Save to file
        output_file = "output_despatch.xml"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(xml_output)

        print(f"\nSuccess! Saved to {os.path.abspath(output_file)}")

    except Exception as e:
        print(f" Error during generation: {e}")


if __name__ == "__main__":
    # Test with your multi-item order from mock_orders.json
    run_manual_test("ORDER-002")
