# class Person:
#     name="naveen"
#     age=22
#     gender="male"     #stactic

# obj1=Person() #assing class to object 
# obj2=Person()
# print(obj1)
# print(obj2) # which class and object location


# print(obj1.name) # printing the name
# print(obj2.name)

# obj1.name="naveen kuamr" #updating name
# print(obj1.name)
# print(obj2.name)

# dynamic objects
# class Person:
#     def __init__(self,name,gender,age):
#         self.name=name
#         self.gender=gender
#         self.age=age
# obj_rakesh=Person("kiran","male",23)
# obj_ragu=Person("ragu","male",24)
# print(obj_rakesh.name)
# print(obj_ragu.name)


# class Media:
#     def __init__(self,app,color,purpose):
#         self.app=app
#         self.color=color
#         self.purpose=purpose

#     def purpose1(self):
#         print("my nmae is naveen")
# obj_app=Media("instgram","red","entertinement")
# obj_news=Media("way2news","white and orange","loacl news")
# obj_internet=Media("youtube","red","chill")
# print(obj_app.app,obj_app.color,obj_app.purpose)
# print(obj_news.app,obj_news.color,obj_news.purpose)
# print(obj_internet.app,obj_internet.color,obj_internet.purpose)
# obj1=Media("kiran","red","enjoy")
# print(obj1.app)


# bank acccount class

class BankAccount():
    def __init__(acc,name,email,ph,balance):
        acc.name=name
        acc.email=email
        acc.ph=ph
        acc.balance=balance
    def deposit(acc,d_amount):
        acc.balance+=d_amount
    def withdraw(acc,w_amount):
        acc.balance-=w_amount
    def checkbalance(acc):
        print(acc.balance)
navee_acc=BankAccount("naeen","naveen@gmail.com",9704570356,10000)
navee_acc.checkbalance()
navee_acc.deposit(5000)
navee_acc.checkbalance()
navee_acc.withdraw(5000)
navee_acc.checkbalance()


