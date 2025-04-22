from datetime import datetime
from config import DAILY_WITHDRAWAL_LIMIT, MAX_PIN_ATTEMPTS
from exceptions import (
    CardBlockedException,
    InsufficientFundsException,
    DailyLimitExceededException,
    ATMException,
)

class Account:
    def __init__(self, pin: str, balance: int):
        self.pin = pin
        self.balance = balance
        self.daily_withdrawn = 0
        self.last_withdrawal_date = datetime.now().date()
        self.pin_attempts = 0
        self.card_blocked = False

    def validate_pin(self, entered_pin: str):
        if self.card_blocked:
            raise CardBlockedException("Card is blocked due to multiple invalid PIN attempts.")
        if entered_pin != self.pin:
            self.pin_attempts += 1
            if self.pin_attempts >= MAX_PIN_ATTEMPTS:
                self.card_blocked = True
                raise CardBlockedException("Card blocked after 3 invalid PIN attempts.")
            raise ATMException("Invalid PIN.")
        self.pin_attempts = 0

    def can_withdraw(self, amount: int):
        if self.balance < amount:
            raise InsufficientFundsException("Insufficient account balance.")

        today = datetime.now().date()
        if self.last_withdrawal_date != today:
            self.daily_withdrawn = 0
            self.last_withdrawal_date = today

        if self.daily_withdrawn + amount > DAILY_WITHDRAWAL_LIMIT:
            raise DailyLimitExceededException("Daily withdrawal limit exceeded.")

    def withdraw(self, amount: int):
        self.can_withdraw(amount)
        self.balance -= amount
        self.daily_withdrawn += amount
