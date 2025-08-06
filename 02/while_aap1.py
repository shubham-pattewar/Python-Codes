# Write a PYTHON program to check the entered number is prime or not

n = int(input("Enter a Number: "))
i = 2

while(i<=n):
    if(n % i == 0):
        print("Not Prime")
        break
    i+=1
else:
    print("Yes Prime")