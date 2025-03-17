import MySQLdb
from config import DB_CONFIG


def get_db_connection():
    return MySQLdb.connect(
        user=DB_CONFIG["USER"],
        password=DB_CONFIG["PASSWORD"],
        host=DB_CONFIG["HOST"],
        database=DB_CONFIG["DATABASE"],
    )


def insert_order(order):
    try:
        db_connection = get_db_connection()
        cursor = db_connection.cursor()

        cursor.execute(
            """
            INSERT INTO orders (product, price, quantity, shipping_method, discount, shipping_cost, sub_total, total_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                order["product"],
                order["price"],
                order["quantity"],
                order["shipping_method"],
                order["discount"],
                order["shipping_cost"],
                order["sub_total"],
                order["total_amount"],
            ),
        )

        db_connection.commit()
        order_id = cursor.lastrowid

        cursor.close()
        db_connection.close()

        return order_id, None
    except Exception as e:
        return None, str(e)
