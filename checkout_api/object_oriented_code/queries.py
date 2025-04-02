INSERT_ORDER = "INSERT INTO orders_oop (customer_name) VALUES (%s)"

INSERT_ORDER_ITEM = """
    INSERT INTO order_items_oop (order_id, product, price, quantity, shipping_method, discount, shipping_cost, sub_total, total_amount)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

FETCH_ORDER = "SELECT * FROM orders_oop WHERE id = %s"

FETCH_ORDER_ITEMS = (
    "SELECT product, price, quantity FROM order_items_oop WHERE order_id = %s"
)

FETCH_ORDER_CALCULATIONS = """
    SELECT shipping_method, shipping_cost, sub_total, total_amount, discount 
    FROM order_items_oop WHERE order_id = %s LIMIT 1
"""
