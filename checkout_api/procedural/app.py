from flask import Flask, request, jsonify
from order_calculations import compute_order_cost
from db_operations import insert_order


app = Flask(__name__)


def validate_order(order):
    try:
        product = str(order["product"])
        price = float(order["price"])
        quantity = int(order["quantity"])
        shipping_method = str(order["shipping_method"])

        return {
            "product": product,
            "price": price,
            "quantity": quantity,
            "shipping_method": shipping_method,
        }, None
    except (KeyError, ValueError) as e:
        return None, str(e)


@app.route("/create_orders", methods=["POST"])
def create_orders():
    data = request.get_json()

    if not isinstance(data, list):
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "Invalid input: Expected a list of orders",
                }
            ),
            400,
        )

    order_ids = []
    for order in data:
        validated_order, error = validate_order(order)
        if error:
            return (
                jsonify({"status": "error", "message": f"Invalid order data: {error}"}),
                400,
            )

        final_order = compute_order_cost(validated_order)

        order_id, db_error = insert_order(final_order)
        if db_error:
            return (
                jsonify({"status": "error", "message": f"Database error: {db_error}"}),
                500,
            )

        order_ids.append(order_id)

    return (
        jsonify(
            {
                "status": "success",
                "message": "Orders created successfully",
                "order_ids": order_ids,
            }
        ),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)
