class Order:
    SHIPPING_RATES = {"standard": 50.00, "express": 100.00}

    def __init__(self, product, price, quantity, shipping_method):
        self.product = product
        self.price = price
        self.quantity = quantity
        self.shipping_method = shipping_method

        self.discount = 0.00
        self.shipping_cost = 0.00
        self.sub_total = 0.00
        self.total_amount = 0.00

    def calculate_discount(self):
        total_price = self.price * self.quantity
        if total_price > 1000:
            self.discount = total_price * 0.10
        elif total_price > 500:
            self.discount = total_price * 0.05

    def calculate_shipping_cost(self):
        self.shipping_cost = self.SHIPPING_RATES.get(self.shipping_method, 0.00)

    def calculate_sub_total(self):
        self.sub_total = self.price * self.quantity

    def calculate_total_amount(self):
        self.total_amount = self.sub_total - self.discount + self.shipping_cost

    def process_order(self):
        self.calculate_discount()
        self.calculate_shipping_cost()
        self.calculate_sub_total()
        self.calculate_total_amount()
