# class Public():
#     def __init__(self):
#         self.name='naveen'

# obj=Public()
# print(obj.name)



# class Protect():
#     def __init__(self):
#         self._name='naveen'

# obj=Protect()
# print(obj._name)



# class Private():
#     def __init__(self):
#         self.__name="naveen"

# obj=Private()
# print(obj._Private__name)



# class Parent():
#     def __init__(self):
#         self.name='naveen'
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print(self.name)

# obj2=Child()



# class Parent():
#     def __init__(self):
#         self._name='naveen'
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print(self._name)

# obj2=Child()


# class Parent():
#     def __init__(self):
#         self.__name='naveen'
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print(self._Parent__name)

# obj2=Child()




# class Sample():
#     def __init__(self):
#         self.name='naveen'
#     def getDetails(self):
#         return self.name
# obj3=Sample() 



class PiggyBank:
    def __init__(self, money):
        self.__money = money  # Private money, hidden inside

    def show_money(self):
        return self.__money  # See how much money is inside

    def add_money(self, amount):
        if amount > 0:
            self.__money += amount
            print("Money added!")
        else:
            print("Invalid amount!")

# Createing a piggy bank with 100
bank = PiggyBank(100)

# See how much money is inside the bank
print("Money in bank:", bank.show_money())

# Add 50 to it
bank.add_money(50)

# See updated amount
print("Updated money:", bank.show_money())

# Try to add a negative amount
bank.add_money(-20)
