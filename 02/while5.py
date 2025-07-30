# Write a PYTHON program to print sum Of Odd numbers up to n
n = int(input("Enter a Number: "))

i = 1
sum = 0
while i <= n:
    sum += i
    i += 2

print(f"Sum of all Odd Numbers upto {n}: {sum}")
