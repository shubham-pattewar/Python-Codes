# Function Polymorphism
# same name function but defferent parameters

print(len("Welcome to DYPCET"))
print(len(['ABC', 78, 'DEF', 99, 8]))

print(5 + 10)
print("Hello " + "World")
print([1,2,3] + [4,5,6])


# Class Polymorphism

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.name = age

    def func(self):
        print("This is Employee")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.name = age
    def func(self):
        print("Student")

class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.name = age
    def func(self):
        print("Teacher")

e1 = Employee("shubham", 32)
s1 = Student("Pratik", 22)
t1 = Teacher("Harsh", 43)

for i in (e1, s1, t1):
    i.func()


