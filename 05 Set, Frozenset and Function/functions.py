# Simple Function
def simple_fun():
    print("Hello There")

simple_fun()            #calling function


# Parameterised Function
def para_fun(n1, n2):
    print("Multiplication is: ", n1 + n2)

para_fun(6,75)


# default argument in function
def default_argument(n1, n2 = 30, n3 = 40):
    print("Sum of all: ", (n1+ n2+ n3))
    print("Product of all: ", (n1*n2*n3))
    print("Num 1: ", n1)
    print("Num 2: ", n2)
    print("Num 3: ", n3)

default_argument(10)
default_argument(10, 20)
default_argument(10, 50, 90)


# lambda function
x = lambda a : a + 25
print(x(10))


y = lambda a,b : a * b
print(y(20,50))


def func(n):
    return lambda a: a*n

variable = func(10)
print(variable(2))
