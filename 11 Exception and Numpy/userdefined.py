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