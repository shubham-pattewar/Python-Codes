# Reading a file
file = open("myfile.txt", "r")
data = file.read()
print(data)
file.close()


# writing some data in the file
with open('myfile.txt', 'w') as file:           # If the file exists, its content is deleted
    file.write("Hello added a line\n")
    file.write("Hey there added a new line\n")


# append content in the file
with open('myfile.txt', "a") as file:           # append will add to next line
    file.write("Writing after append\n")


# binary mode
with open('navig.png', 'rb') as file:
    data = file.read()
    print(data)






