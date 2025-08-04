# Write a PYTHON program to print sum of even numbers up to n
n = int(input("Enter a Number: "))

i = 2
sum = 0
while i <= n:
    sum += i
    i += 2

print(f"Sum of all Even Numbers upto {n}: {sum}")

