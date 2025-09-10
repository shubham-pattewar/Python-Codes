# Default Constructor
class Vehicle:
    def __init__(self):
        self.type = "Car"
        self.model = "Toyoto"
        self.year = 2022
    
veh1 = Vehicle()
print("Type:", veh1.type)
print("Model:", veh1.model)
print("Year:", veh1.year)


# Parameterised Constructor
class Animal:
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age

anim1 = Animal("Dog", "Tom", 12)
print("Animal Type:", anim1.type)
print("Animal Name:", anim1.name)
print("Animal Age:", anim1.age)

anim2 =Animal("Cat", "Jerry", 6)
print("Animal Type:", anim2.type)
print("Animal Name:", anim2.name)
print("Animal Age:", anim2.age)