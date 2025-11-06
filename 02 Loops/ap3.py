a = int(input("Enter 1st No: "))
b = int(input("Enter 2st No: "))
c = int(input("Enter 3st No: "))

if a<b and a<c:
    print(f"{a} is smallest")
elif b<a and b<c:
    print(f"{b} is smallest")
else:
    print(f"{c} is smallest")