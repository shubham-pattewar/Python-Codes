# Compile Time Polymorphism => Method Overloading

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a+b+c
    
    def mul(self, a=1, b=1, c=1):
        return a*b*c
    
c = Calculator()
print(c.add())
print(c.add(1))
print(c.add(2,3))
print(c.add(4,6,7))

print(c.mul())
print(c.mul(3))
print(c.mul(3,2))
print(c.mul(6,7,8))


