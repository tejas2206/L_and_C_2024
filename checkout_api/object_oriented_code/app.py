from flask import Flask, request, jsonify
from order_service import OrderService
from dto import OrderDTO

app = Flask(__name__)
order_service = OrderService()


@app.route("/create_order_oop", methods=["POST"])
def create_order():
    """API endpoint to create orders"""
    data = request.get_json()
    order_data, error = OrderDTO(data)

    if error:
        return jsonify({"status": "error", "message": error}), 400

    order_id, db_error = order_service.create_order(order_data)

    if db_error:
        return (
            jsonify({"status": "error", "message": f"Database error: {db_error}"}),
            500,
        )

    return (
        jsonify(
            {
                "status": "success",
                "message": "Order created successfully",
                "order_id": order_id,
            }
        ),
        201,
    )


@app.route("/get_order_oop/<int:order_id>", methods=["GET"])
def fetch_order(order_id):
    """API endpoint to fetch an order by ID."""
    order, error = order_service.get_order(order_id)

    if error:
        return jsonify({"status": "error", "message": error}), 404

    return jsonify({"status": "success", "order": order})


if __name__ == "__main__":
    app.run(debug=True)
