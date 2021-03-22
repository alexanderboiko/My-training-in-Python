
#Publik protected private attr and methods

class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    # def print_public_data(self):
    #     print(self.name,self.balance, self. passport)

    # def print_protected_data(self):
        # print(self._name,self._balance, self._passport)

    def print_private_data(self):
        print(self.__name,self.__balance, self.__passport)

account1 = BankAccount('Bob', 10000000, 3720132)
account1.print_private_data()
print(dir(account1))
# print(account1.__name)
# print(account1.__balance)
# print(account1.__passport)