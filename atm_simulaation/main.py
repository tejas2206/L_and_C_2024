from atm import ATM
from account import Account
from service import ATMService
from exceptions import ATMException, CardBlockedException

def main():
    atm = ATM(total_cash=100000)
    account = Account(pin="1234", balance=45000)
    service = ATMService(atm, account)

    print("Welcome to Python ATM Simulation.\n")

    while True:
        try:
            pin = input("Enter your 4-digit PIN: ")
            amount_input = input("Enter withdrawal amount (₹): ")

            if not amount_input.isdigit():
                raise ValueError("Withdrawal amount must be a number.")

            amount = int(amount_input)

            service.withdraw_money(pin, amount)

        except CardBlockedException as e:
            print(f"{e}")
            print("Your card has been blocked. Exiting.")
            break
        except ATMException as e:
            print(f"ATM Error: {e}")
        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        print("\nDo you want to perform another transaction?")
        choice = input("Type 'y' to continue or anything else to exit: ").lower()
        if choice != 'y':
            print("Thank you for using Python ATM. Goodbye!")
            break

if __name__ == "__main__":
    main()
