from flask import Flask, request, jsonify
from order_calculations import Order
from db_operations import DatabaseManager

app = Flask(__name__)

def validate_order(order_data):
    try:
        return Order(
            product=str(order_data["product"]),
            price=float(order_data["price"]),
            quantity=int(order_data["quantity"]),
            shipping_method=str(order_data["shipping_method"]),
        ), None
    except (KeyError, ValueError) as e:
        return None, str(e)

@app.route("/create_orders_oop", methods=["POST"])
def create_orders_oop():
    """API to handle multiple order creation requests."""
    data = request.get_json()

    if not isinstance(data, list):
        return jsonify({"status": "error", "message": "Invalid input: Expected a list of orders"}), 400

    db = DatabaseManager()
    order_ids = []

    for order_data in data:
        order, error = validate_order(order_data)
        if error:
            db.close()
            return jsonify({"status": "error", "message": f"Invalid order data: {error}"}), 400

        order.process_order()

        order_id, db_error = db.insert_order(order)
        if db_error:
            db.close()
            return jsonify({"status": "error", "message": f"Database error: {db_error}"}), 500

        order_ids.append(order_id)

    db.close()

    return jsonify({"status": "success", "message": "Orders created successfully", "order_ids": order_ids}), 201

if __name__ == "__main__":
    app.run(debug=True)