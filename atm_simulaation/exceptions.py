class ATMException(Exception):
    pass

class InsufficientFundsException(ATMException):
    pass

class InsufficientATMFundsException(ATMException):
    pass

class ServerConnectionException(ATMException):
    pass

class DailyLimitExceededException(ATMException):
    pass

class CardBlockedException(ATMException):
    pass
