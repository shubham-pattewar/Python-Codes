# Write a PYTHON program to print Fibonacci series up to n

n = int(input("Enter a Number: "))
x = 1
y = 2
z = 0
while x < n:
    z = x + y
    print (z, end = ' ')
    x = y
    y = z