class Student:
    def func1(self):
        print("I am a Student")

class Exam(Student):
    def func2(self):
        print("Prepare for Exam!!!")

class Project:
    def func3(self):
        print("Prepare for the Project")

class Result(Exam, Project):
    def func4(self):
        print("Result: Project Marks + Exam Marks")


obj1 = Result()
obj1.func1()
obj1.func2()
obj1.func3()
obj1.func4()

obj2 = Project()
# obj2.func1()      # Error will occur
# obj2.func2()      # Error will occur
obj2.func3()
# obj2.func4()      # Error will occur

obj3 = Exam()
obj3.func1()        
obj3.func2()
# obj3.func3()        # Error will occur
# obj3.func4()        # Error will occur

