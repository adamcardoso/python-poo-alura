class Client:
    def __init__(self, name):
        self.__name = name

    @property  # property decorator is used to make a method a property
    def name(self):
        return self.__name.title()  # title() method capitalizes the first letter of each word

    @name.setter  # setter decorator is used to set the value of a property
    def name(self, name):
        self.__name = name
