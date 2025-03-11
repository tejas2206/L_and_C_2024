from flask import Flask, request, jsonify
import MySQLdb

app = Flask(__name__)

def get_db_connection():
    return MySQLdb.connect(user='root', password='sHASHI&456',
                           host='localhost', database='checkout_db')

def calculate_shipping_cost(shipping_method):
    if shipping_method == 'standard':
        return 50.00
    elif shipping_method == 'express':
        return 100.00
    else:
        return 0.00

def calculate_totals(price, quantity, discount, shipping_cost):
    sub_total = price * quantity
    total_amount = sub_total - discount + shipping_cost
    return sub_total, total_amount

@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.get_json()
    product = data['product']
    price = data['price']
    quantity = data['quantity']
    shipping_method = data['shipping_method']
    payment_method = data['payment_method']
    discount = data['discount']

    shipping_cost = calculate_shipping_cost(shipping_method)
    sub_total, total_amount = calculate_totals(price, quantity, discount, shipping_cost)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO orders (product, price, quantity, shipping_method, payment_method, discount, shipping_cost, sub_total, total_amount)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (product, price, quantity, shipping_method, payment_method, discount, shipping_cost, sub_total, total_amount))
    conn.commit()
    order_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return jsonify({
        'message': 'Order created successfully',
        'order_id': order_id,
    })

if __name__ == '__main__':
    app.run(debug=True)
