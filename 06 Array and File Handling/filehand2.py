# Read from one file anf write in another file

with open("myfile.txt", "r") as file1:
    data2 = file1.read()

with open("hisfile.txt", "w") as file2:
    file2.write(data2)


# Seek and tell Function
with open("myfile.txt", 'r+') as f:
    f.seek(7)
    f.write("***NEW TEXT***")
    print(f.tell())

