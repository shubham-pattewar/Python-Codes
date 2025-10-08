class Vehicle:
    def func1(self):
        print("It is an Vehicle")

class Bikes(Vehicle):
    def func2(self):
        print("The Vehicle is Bike")

class Cars(Vehicle):
    def func3(self):
        print("The Vehicle is Car")

class Buses(Vehicle):
    def func4(self):
        print("The Vehicke is a Bus")

class Trucks(Vehicle):
    def func4(self):
        print("The Vehicle is a Truck")


obj1 = Trucks()
obj1.func4()
obj1.func1()

obj2 = Cars()
obj2.func3()
obj2.func1()