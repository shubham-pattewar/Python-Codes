class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal Name: ", self.name)

class Dog(Animal):
    def getName(self):
        print("Dog Name: ", self.name)


obj = Dog("Tommy")
obj.display()
obj.getName()

obj2 = Dog("Jack")
obj2.display()
obj2.getName()