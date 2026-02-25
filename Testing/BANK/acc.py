class Account:
    def __init__(self):
        self.balance = 1000

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance