def calculate_sub_total(items):
    return sum(item["price"] * item["quantity"] for item in items)


def calculate_discount(sub_total):
    if sub_total > 1000:
        return sub_total * 0.10
    elif sub_total > 500:
        return sub_total * 0.05
    return 0.00


def determine_shipping_method(items):
    return "express" if any(item["price"] > 500 for item in items) else "standard"


def calculate_shipping_cost(shipping_method):
    return 100.00 if shipping_method == "express" else 50.00


def calculate_total_amount(sub_total, discount, shipping_cost):
    return sub_total - discount + shipping_cost


def calculate_order_totals(items):
    sub_total = calculate_sub_total(items)
    discount = calculate_discount(sub_total)
    shipping_method = determine_shipping_method(items)
    shipping_cost = calculate_shipping_cost(shipping_method)
    total_amount = calculate_total_amount(sub_total, discount, shipping_cost)

    return sub_total, discount, shipping_cost, total_amount, shipping_method
