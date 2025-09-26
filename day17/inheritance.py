#accuring methods and attributes form already defined class into newly created
# class is called inheritance

#creating a new class from already created class is called
# example  children get geans from parents is called 

# types of inheritance:
# 1) single inheritance: if we are creating a sub class from single class
# 2) multiple inheritance: if we are creating single class from multiple class is called 
# 3) multilevel inheritance:
# 4) hierarchical inheritance:
# 5) hybrid inheritance:




# class Parent():
#     def Pmethod(self):
#         print(" i am a method from parent class: ")
#     def Pmethod2(self):
#         print("i am a second method of parent: ")
    
# class Child(Parent):
#     def Cmethod(self):
#         print(" i am a method from child: ")
#         super().Pmethod2()  #calling method from super class using super( )
        

# obj1=Child()
# obj1.Cmethod()
# obj1.Pmethod()
# obj1.Pmethod2()


class user():
    def __init__(self,name,email):
        self.name=name
        self.email=email
class Student(user):
    def __init__(self,name,email,enrolled_course):
       super().__init__(name,email)
       self.enrolled_course=enrolled_course
    def getCources(self):
        print(f"{self.name} is learning {self.enrolled_course}")
    def removeCourse(self,course):
        self.enrolled_course.remove(course)
        self.getCources()
    def addcourse(self,course):
        self.enrolled_course.append(course)
        self.getCources()

class Instructor(user):
    def __init__(self,name,email,course_trained):
        super().__init__(name,email)
        self.course_trained=course_trained
    def getcources(self):
        print(f"{self.name} is teaching {self.course_trained}")


Student_obj=Student("naveen","naveen@gmail.com",["html","css","js","powerBi"])
# Student_obj.getCources()
# Trainer_obj=Instructor("harish","harish@gmail.com",["frontend","backend","db","Ai"])
# Trainer_obj.getcources()
Student_obj.removeCourse("html")
Student_obj.addcourse("python")