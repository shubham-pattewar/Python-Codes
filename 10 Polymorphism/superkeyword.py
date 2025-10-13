class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()


class Animal:
    def __init__(self):
        print("This is the Animal class")

class Dog(Animal):
    def __init__(self):
        super().__init__()   # calls the parent class constructor
        print("This is the Dog class")

# Create object
d = Dog()

