class MinorError(Exception):
    "Age must be greater than 18"
    pass

class MajorError(Exception):
    "Age is too high"
    pass

try:
    age = int(input("Enter Age: "))
    if age < 18:
        raise MinorError("Age must be atleast 18")
    elif age > 100:
        raise MajorError("Age must be less than 100")
    else:
        print("You are eligible to vote")

except MinorError as e:
    print("Error: ", e)

except MajorError as e:
    print("Error: ", e)




# Define a custom exception
class MyCustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

# Function that may raise the custom exception
def check_number(number):
    if number < 0:
        raise MyCustomException(f"Number cannot be negative: {number}")
    else:
        print(f"Number is valid: {number}")

# Using the custom exception
try:
    check_number(10)   # Valid
    check_number(-5)   # This will raise the custom exception
except MyCustomException as e:
    print(f"Caught exception: {e}")
