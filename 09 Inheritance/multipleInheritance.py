class Wheel:
    def func1(self):
        print("It's a Wheel")

class Rubber:
    def func2(self):
        print("Rubber")

class Tyre(Wheel, Rubber):
    def func3(self):
        print("Tyre = Wheel + Rubber")

obj1 = Tyre()
obj1.func1()
obj1.func2()
obj1.func3()
