# # method overriding: replacing or changing the logic of method from super class in sub class in subclass is called method overriding.
# # It can be appplicable only when inheritance happens otherwise it won't applicable


# class order:
#     def __init__(self,customer,order_id):
#         self.customer=customer
#         self.order_id=order_id
#     def deliver(self):
#         print(f"{self.customer} will get his orde num {self.order_id} the stack order")

# class Express(order):
#     def __init__(self, customer, order_id):
#         super().__init__(customer, order_id)
#     def deliver(self):
#         print(f"{self.customer} the order of the no is {self.order_id} is getting order")

# obj2=order('ramu','bdh324')
# obj2.deliver()
# obj1=Express('hari','jeu2348')
# obj1.deliver()

# print(obj1.__dict__)
# print(obj2.__dict__)

# print(Express.__mro__)
# print(order.__mro__)

# print(Express.mro())
# print(order.mro())


class Vechicle:
    def start(self):
        print("vechicle is starting...")

class Car(Vechicle):
    def start(self):
        print("car is starting with a key!")

Vechicle=Vechicle()
Car=Car()
Vechicle.start()
Car.start()
