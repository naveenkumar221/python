# class Parent1():
#     def Pmethod(self):
#         print("i am method from parent1: ")
# class Parent2():
#     def p2method(self):
#         print(" i am a method from parent2:")
# class Child(Parent1,Parent2):
#     def Cmethod(self):
#         print(" i am a method from child: ")
#         super().Pmethod()
#         super().p2method()
# obj1=Child()
# obj1.Cmethod()
# obj1.p2method()
# obj1.Pmethod()p


# class parent_actor():
#     def __init__(self,name,Pworth):
#         self.Pname=name
#         self.Pworth=Pworth
#         print(f"{self.Pname} is the parent:")
#     def passets(self):
#         print(f"{self.Pname} assets is {self.Pworth}")
# class Child_actor(parent_actor):
#     def __init__(self,Pname,Cname,Pworth):
#         super().__init__(Pname,Pworth)
#         self.Cname=Cname
#         print(f"{self.Cname} is the cild of the {self.Pname}")
#     def Cassets(self,worth):
#         self.Cworth=worth
#         print(f"{self.Cname} is having worth of {self.Cworth}cr")
#     def TotalAssets(self):
#         print(f"total assets of {self.Cname} is {self.Pworth+self.Cworth}")
# ramcharan=Child_actor("chiranjeevi","ramcharan",100)
# ramcharan.Cassets(30)
# ramcharan.TotalAssets()
# ramcharan.passets()

        


class A():
    def display(self):
        print("A class")
class B():
    def display(self):
        print("B class")
class C(A,B):
    def display(self):
        A().display()
        print("C class")
        B().display()
obj=C()
obj.display()

