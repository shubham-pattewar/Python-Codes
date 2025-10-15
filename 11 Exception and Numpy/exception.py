# ZeroDivisionError
# n = 20
# result = n/0
# print(result)


# Handling Exception
no = int(input("Enter a Number: "))
try:
    res = 100/no

except ZeroDivisionError:
    print("You can't divide by Zero")

except ValueError:
    print("Enter a valid String")

else:
    print("Result is: ", res)

finally:
    print("Execution Completed")            # runs all the time

