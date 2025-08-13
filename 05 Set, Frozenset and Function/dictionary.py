student = {"Name":"Shubham", "Roll":25, "Class":"TYA", "Subject":"APC"}

print(student)
print("Name is ", student["Name"])
print("Class is ", student["Class"])

for i in student:
    print(i)            # it will print all keys


# Dictionary Methods
student2 = {"Name":"Shubham", "Roll":25, "Class":"TY", "Subject":"APC", "Div":"A" }
student3 = {"Name":"Anuj", "Roll":27}

print(student2.get("Class"))

print(student2.update(student3))
print(student2)
