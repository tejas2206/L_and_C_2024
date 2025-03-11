from flask import Flask, request, jsonify
from extensions import db
from models import Order

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sHASHI&456@localhost/checkout_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    @app.route('/oop_create_order', methods=['POST'])
    def oop_create_order():
        data = request.get_json()
        new_order = Order(
            product=data['product'],
            price=data['price'],
            quantity=data['quantity'],
            shipping_method=data['shipping_method'],
            payment_method=data['payment_method'],
            discount=data.get('discount', 0.00),
            shipping_cost=calculate_shipping_cost(data['shipping_method']),
            sub_total=data['price'] * data['quantity'],
            total_amount=(data['price'] * data['quantity']) - data.get('discount', 0.00) + calculate_shipping_cost(data['shipping_method'])
        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify({'message': 'Order created successfully', 'order_id': new_order.id})

    return app

def calculate_shipping_cost(shipping_method):
    if shipping_method == 'standard':
        return 50.00
    elif shipping_method == 'express':
        return 100.00
    else:
        return 0.00
