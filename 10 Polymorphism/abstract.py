from abc import ABC, abstractmethod

class Car(ABC):
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("Mileage: 30kmph")
    
class Suzuki(Car):
    def mileage(self):
        print("Mileage: 20kmph")

t = Tesla()
t.mileage()

s = Suzuki()
s.mileage()