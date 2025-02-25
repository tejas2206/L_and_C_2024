class Wallet:
    def __init__(self, initial_balance: float):
        self.__balance = initial_balance

    def get_total_money(self) -> float:
        return self.__balance

    def __subtract_money(self, amount: float):
        self.__balance -= amount

    def add_money(self, amount: float):
        self.__balance += amount

    def make_payment(self, amount: float) -> bool:
        if self.__balance >= amount:
            self.__subtract_money(amount)
            return True
        return False


class Customer:
    def __init__(self, first_name: str, last_name: str, initial_balance: float):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__wallet = Wallet(initial_balance)

    def get_first_name(self) -> str:
        return self.__first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def make_payment(self, amount: float) -> bool:
        return self.__wallet.make_payment(amount)


# Client code
customer = Customer("Tejas", "Kumar", 10.00)
payment = 2.00  # "I want my two dollars!"

if customer.make_payment(payment):
    print("Payment successful!")
else:
    print("Come back later for payment.")
