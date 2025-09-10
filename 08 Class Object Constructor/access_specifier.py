class Student:
    def __init__(self, name, roll):
        self.name = name          # Public attribute
        self._college = "DYPCET"     # Protected attribute
        self.__marks = 85         # Private attribute

    def show(self):
        print("Name:", self.name)
        print("College:", self._college)
        print("Marks:", self.__marks)

s1 = Student("Shubham", 101)

print(s1.name)

print(s1._college)

# print(s1.__marks)   # AttributeError

s1.show()
