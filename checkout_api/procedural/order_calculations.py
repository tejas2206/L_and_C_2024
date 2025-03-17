def calculate_shipping_cost(shipping_method):
    shipping_rates = {"standard": 50.00, "express": 100.00}
    return shipping_rates.get(shipping_method, 0.00)


def calculate_discount(price, quantity):
    total_price = price * quantity
    if total_price > 1000:
        return total_price * 0.10
    elif total_price > 500:
        return total_price * 0.05
    return 0.00


def calculate_sub_total(price, quantity):
    return price * quantity


def calculate_total_amount(sub_total, discount, shipping_cost):
    return sub_total - discount + shipping_cost


def compute_order_cost(order):
    shipping_cost = calculate_shipping_cost(order["shipping_method"])
    discount = calculate_discount(order["price"], order["quantity"])
    sub_total = calculate_sub_total(order["price"], order["quantity"])
    total_amount = calculate_total_amount(sub_total, discount, shipping_cost)

    order.update(
        {
            "discount": discount,
            "shipping_cost": shipping_cost,
            "sub_total": sub_total,
            "total_amount": total_amount,
        }
    )
    return order
