def validate_order_data(data):
    if not isinstance(data, dict) or "customer_name" not in data or "items" not in data:
        return None, "Invalid order format. Must include 'customer_name' and 'items'."

    if not isinstance(data["items"], list) or len(data["items"]) == 0:
        return None, "Order must contain at least one item."

    try:
        order_dto = {
            "customer_name": str(data["customer_name"]),
            "items": [
                transform_item_data(item) for item in data["items"]
            ]
        }
        return order_dto, None

    except (KeyError, ValueError) as e:
        return None, f"Invalid order item: {str(e)}"


def transform_item_data(item):
    return {
        "product": str(item["product"]),
        "price": float(item["price"]),
        "quantity": int(item["quantity"]),
    }
