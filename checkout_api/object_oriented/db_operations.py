import MySQLdb
from config import DB_CONFIG


class DatabaseManager:
    def __init__(self):
        self.connection = MySQLdb.connect(
            user=DB_CONFIG["USER"],
            password=DB_CONFIG["PASSWORD"],
            host=DB_CONFIG["HOST"],
            database=DB_CONFIG["DATABASE"],
        )
        self.cursor = self.connection.cursor()

    def insert_order(self, order):
        try:
            self.cursor.execute(
                """
                INSERT INTO order_summary
                (product, price, quantity, shipping_method, discount, shipping_cost, sub_total, total_amount) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    order.product,
                    order.price,
                    order.quantity,
                    order.shipping_method,
                    order.discount,
                    order.shipping_cost,
                    order.sub_total,
                    order.total_amount,
                ),
            )

            self.connection.commit()
            return self.cursor.lastrowid, None
        except Exception as e:
            return None, str(e)

    def close(self):
        self.cursor.close()
        self.connection.close()
