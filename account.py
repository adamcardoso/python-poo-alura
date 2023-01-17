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

    def __can_withdraw(self, amount_to_withdraw):  # using two underscores to make it private
        amount_available_for_withdraw = self.__balance + self.__limit
        return amount_to_withdraw <= amount_available_for_withdraw

    def withdraw(self, amount):
        if self.__can_withdraw(amount):
            self.__balance -= amount
        else:
            print("Insufficient funds")

    # encapsulation
    def transfer(self, amount, destination_account):
        self.withdraw(amount)
        destination_account.deposit(amount)

    # getters and setters
    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @property  # property decorator is used to make a method a property
    def limit(self):
        return self.__limit

    @limit.setter  # setter decorator is used to set the value of a property
    def limit(self, limit):
        self.__limit = limit
    # end of getters and setters

    @staticmethod  # static method decorator is used to make a method a static method
    def bank_code():
        return "001"

    @staticmethod
    def all_bank_codes():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
