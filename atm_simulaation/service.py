from exceptions import ATMException

class ATMService:
    def __init__(self, atm, account):
        self.atm = atm
        self.account = account

    def withdraw_money(self, pin: str, amount: int):
        try:
            self.account.validate_pin(pin)
            self.account.can_withdraw(amount)
            cash = self.atm.withdraw_cash(amount)
            self.account.withdraw(amount)
            print(f"Withdrawal successful: ₹{cash}")
            print(f"Remaining account balance: ₹{self.account.balance}")
            print(f"Remaining ATM balance: ₹{self.atm.total_cash}")
        except ATMException as e:
            print(f"Error: {e}")
