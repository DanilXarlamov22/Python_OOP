class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
        if self._balance < 0:
            raise ValueError("На счете недостаточно средств")

    def transfer(self, account, amount):
        self.withdraw(amount)
        account.deposit(amount)
