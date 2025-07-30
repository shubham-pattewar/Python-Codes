# Write a PYTHON program to print natural numbers up to n in reverse order.
n = int(input("Enter a Number: "))  

print("Natural Numbers in Reverse: ")
while n != 0:
    print(n, end = '  ')
    n -= 1