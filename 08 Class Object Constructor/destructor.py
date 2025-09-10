# Destructor
class Employee:
    def __init__(self):
        print("Employee Created")

    def __del__(self):
        print("Employee Deleted")

emp1 = Employee()
del emp1            # deleting employee


