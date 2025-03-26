from flask import Flask, request, jsonify
from db_operations import insert_order, get_order
from dto import validate_order_data

app = Flask(__name__)


@app.route("/create_order", methods=["POST"])
def create_order():
    """API endpoint to create order."""
    data = request.get_json()
    order_data, error = validate_order_data(data)

    if error:
        return jsonify({"status": "error", "message": error}), 400

    order_id, db_error = insert_order(order_data)

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


@app.route("/get_order/<int:order_id>", methods=["GET"])
def fetch_order(order_id):
    """API endpoint to fetch an order by ID."""
    order, error = get_order(order_id)

    if error:
        return jsonify({"status": "error", "message": error}), 404

    return jsonify({"status": "success", "order": order})


if __name__ == "__main__":
    app.run(debug=True)
