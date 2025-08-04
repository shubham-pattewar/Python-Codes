# Write a PYTHON program to print Fibonacci series up to n

n = int(input("Enter a Number: "))
x = 0
y = 1
while x < n:
    z = x + y

    if z>n:
        break

    print (z, end = ' ')
    x = y
    y = z