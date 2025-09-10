# Class Object

class pet:          # Creating class
    species = "cat"

    def __init__(self, name, age):          #constructor
        self.name = name    
        self.age = age

cat1 = pet("Tom", 5)        # creating object
cat2 = pet("Jerry", 6)

print("Pet 1 Details: ")
print(cat1.name, cat1.age)
print("Pet 2 Details: ")
print(cat2.name, cat2.age)



