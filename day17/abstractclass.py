from abc import ABC, abstractmethod

class Vechile(ABC):
    @abstractmethod
    def vechile_wheelr(self):
        pass

class Bike(Vechile):
    def vechile_wheelr(self):
        print('it is a 2 wheeler model:')

class Car(Vechile):
    def vechile_wheelr(self):
        print("it is a four wheeler model: ")

class Lorry(Vechile):
    def vechile_wheelr(self):
       print("it is a 12 wheeler mode: ")

b=Bike()
c=Car()
l=Lorry()

b.vechile_wheelr()
c.vechile_wheelr()
l.vechile_wheelr()