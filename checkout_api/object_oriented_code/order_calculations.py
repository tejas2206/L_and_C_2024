class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = [OrderItem(**item) for item in items]

    def calculate_sub_total(self):
        return sum(item.calculate_item_total() for item in self.items)

    def calculate_discount(self):
        sub_total = self.calculate_sub_total()
        if sub_total > 1000:
            return sub_total * 0.10
        elif sub_total > 500:
            return sub_total * 0.05
        return 0.00

    def determine_shipping_method(self):
        return "express" if any(item.price > 500 for item in self.items) else "standard"

    def calculate_shipping_cost(self):
        return 100.00 if self.determine_shipping_method() == "express" else 50.00

    def calculate_total_amount(self):
        sub_total = self.calculate_sub_total()
        discount = self.calculate_discount()
        shipping_cost = self.calculate_shipping_cost()
        return sub_total - discount + shipping_cost


class OrderItem:
    def __init__(self, product, price, quantity):
        self.product = product
        self.price = float(price)
        self.quantity = int(quantity)

    def calculate_item_total(self):
        return self.price * self.quantity
