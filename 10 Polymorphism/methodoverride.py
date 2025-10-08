# Run time Polymorphism => Method Overriding

class Animal:
    def sound(self):
        return "Any Sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

a = Animal()
d = Dog()
c = Cat()

print(a.sound())
print(d.sound())
print(c.sound())

