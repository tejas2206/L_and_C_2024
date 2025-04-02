from order_calculations import Order
from db_operations import DatabaseManager
from queries import (
    INSERT_ORDER,
    INSERT_ORDER_ITEM,
    FETCH_ORDER,
    FETCH_ORDER_ITEMS,
    FETCH_ORDER_CALCULATIONS,
)


class OrderService:
    def create_order(self, order_data):
        """Creates an order in the database."""
        order = Order(order_data.customer_name, [vars(item) for item in order_data.items])

        order_id, error = DatabaseManager.execute_query(
            INSERT_ORDER, (order.customer_name,), return_last_id=True
        )

        if error:
            return None, error

        for item in order.items:
            DatabaseManager.execute_query(
                INSERT_ORDER_ITEM,
                (
                    order_id,
                    item.product,
                    item.price,
                    item.quantity,
                    order.determine_shipping_method(),
                    order.calculate_discount(),
                    order.calculate_shipping_cost(),
                    order.calculate_sub_total(),
                    order.calculate_total_amount(),
                ),
            )

        return order_id, None

    def get_order(self, order_id):
        """Fetches an order from the database."""
        order, error = DatabaseManager.execute_query(
            FETCH_ORDER, (order_id,), fetch_one=True
        )
        if error or not order:
            return None, "Order not found"

        items, _ = DatabaseManager.execute_query(
            FETCH_ORDER_ITEMS, (order_id,), fetch_all=True
        )
        calculations, _ = DatabaseManager.execute_query(
            FETCH_ORDER_CALCULATIONS, (order_id,), fetch_one=True
        )

        if calculations:
            del calculations["discount"]
            del calculations["sub_total"]
            del calculations["shipping_method"]

        order["items"] = items
        order.update(calculations)
        return order, None
