import random
from exceptions import ServerConnectionException, InsufficientATMFundsException

class ATM:
    def __init__(self, total_cash: int):
        self.total_cash = total_cash

    def withdraw_cash(self, amount: int):
        if not self._is_server_connected():
            raise ServerConnectionException("Unable to connect with server.")
        if amount > self.total_cash:
            raise InsufficientATMFundsException("Insufficient cash in ATM.")
        self.total_cash -= amount
        return amount

    @staticmethod
    def _is_server_connected():
        return random.choice([True, True, True, False])  # 75% chance of success
