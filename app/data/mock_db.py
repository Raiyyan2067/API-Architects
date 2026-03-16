import json
import os

# Since this file is in the same folder as the JSON,
# we just look for the filename in the current directory.
JSON_PATH = os.path.join(os.path.dirname(__file__), "mock_orders.json")


def get_order(order_id: str):
    """
    TICKET B-03: Fetches a mock order by its ID.
    Returns the dictionary or None if not found.
    """
    try:
        if not os.path.exists(JSON_PATH):
            print(f"Error: Could not find {JSON_PATH}")
            return None

        with open(JSON_PATH, "r") as file:
            all_orders = json.load(file)
            return all_orders.get(order_id)

    except Exception as e:
        print(f"An error occurred reading mock data: {e}")
        return None


# Quick test logic
if __name__ == "__main__":
    print("Testing Mock DB...")
    test = get_order("ORDER-001")
    if test:
        print(f"Found order: {test.get('order_id')}")
    else:
        print("Order not found or JSON error.")
