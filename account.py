class Account:

    def __init__(self, account_number, owner, balance, limit):
        print("Creating account for {}".format(self))
        self.__account_number = account_number  # using two underscores to make it private
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit

    # method to print the account details
    def bank_statement(self):
        print("Account balance {} for owner {}".format(self.__balance, self.__owner))

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    # encapsulation
    def transfer(self, amount, destination_account):
        self.withdraw(amount)
        destination_account.deposit(amount)

    # getters and setters
    def get_owner(self):
        return self.__owner

    def get_balance(self):
        return self.__balance

    @property  # property decorator is used to make a method a property
    def limit(self):
        return self.__limit

    @limit.setter  # setter decorator is used to set the value of a property
    def limit(self, limit):
        self.__limit = limit
    # end of getters and setters

    def __str__(self):
        return f"Account owner: {self.__owner}"
