import MySQLdb
from config import DB_CONFIG
from order_calculations import calculate_order_totals
from queries import (
    INSERT_ORDER,
    INSERT_ORDER_ITEM,
    FETCH_ORDER,
    FETCH_ORDER_ITEMS,
    FETCH_ORDER_CALCULATIONS,
)


def get_db_connection():
    return MySQLdb.connect(
        user=DB_CONFIG["USER"],
        password=DB_CONFIG["PASSWORD"],
        host=DB_CONFIG["HOST"],
        database=DB_CONFIG["DATABASE"],
    )


def insert_order(order_data):
    """Inserts an order and its items into the database."""
    try:
        db_connection = get_db_connection()
        cursor = db_connection.cursor()

        cursor.execute(INSERT_ORDER, (order_data["customer_name"],))
        order_id = cursor.lastrowid

        sub_total, discount, shipping_cost, total_amount, shipping_method = (
            calculate_order_totals(order_data["items"])
        )

        for item in order_data["items"]:
            cursor.execute(
                INSERT_ORDER_ITEM,
                (
                    order_id,
                    item["product"],
                    item["price"],
                    item["quantity"],
                    shipping_method,
                    discount,
                    shipping_cost,
                    sub_total,
                    total_amount,
                ),
            )

        db_connection.commit()
        cursor.close()
        db_connection.close()

        return order_id, None

    except Exception as e:
        return None, str(e)


def get_order(order_id):
    """Fetches an order with all its items."""
    try:
        db_connection = get_db_connection()
        cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute(FETCH_ORDER, (order_id,))
        order = cursor.fetchone()

        if not order:
            return None, "Order not found"

        cursor.execute(FETCH_ORDER_ITEMS, (order_id,))
        items = cursor.fetchall()

        cursor.execute(FETCH_ORDER_CALCULATIONS, (order_id,))
        calculations = cursor.fetchone()

        if calculations:
            del calculations["discount"]
            del calculations["sub_total"]
            del calculations["shipping_method"]

        cursor.close()
        db_connection.close()

        order["items"] = items
        order.update(calculations)

        return order, None

    except Exception as e:
        return None, str(e)
