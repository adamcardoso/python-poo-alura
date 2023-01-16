class Account:

    def __init__(self, account_number, owner, balance, limit):
        print("Creating account for {}".format(self))
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.limit = limit

    def bank_statement(self):
        print("Account balance {} for owner {}".format(self.balance, self.owner))

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        return f"Account owner: {self.owner}"
