class Mobiles():
    def __init__(self,name,version):
        self.name=name
        self.version=version
    
class Keypad(Mobiles):
    def __init__(self,name,version,price):
        super().__init__(name,version)
        self.price=price
obj1=Mobiles("mi",15)
print(obj1.name)
print(obj1.version)
obj2=Keypad("nokika",1500,15)
print(obj2.name,obj2.price,obj2.version)
