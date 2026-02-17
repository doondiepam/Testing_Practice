class BankAccount:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Invalid account")
        self.withdraw(amount)
        other_account.deposit(amount)
        return self.balance, other_account.balance
