class BankAccount:

    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError(
                "Deposit must be positive"
            )

        self._balance += amount

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Withdrawal must be positive"
            )

        if amount > self._balance:
            raise ValueError(
                "Insufficient funds"
            )

        self._balance -= amount

    def get_balance(self):
        return self._balance