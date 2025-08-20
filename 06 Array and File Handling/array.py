import array as arr

# Creating Array
a = arr.array('i', [33, 76, 88, 33])
b = arr.array('d', [4.5, 6.6, 7.8, 9.8, 9.666])


# Print all elements of an aray
print("Array 1: ")
for i in range(0,4):
    print(a[i])

b = arr.array('d', [4.5, 6.6, 7.8, 9.8, 9.666])
print("Array 2: ")
for i in range(0,5):
    print(b[i])


# Accessing elements of an array
print("a[0] = ", a[0])
print("b[2] = ", b[2])


# Adding Elements to an array
a.insert(3, 6)          # inserts 6 at 3rd Index
print(*a)


# Removing elements from array
import array as arr
c = arr.array('i', [1,3,5,7,3,2,3,2,5])
print(c)

c.remove(3)     # removes 1st Occurence of 3
print(c)

c.pop(4)        # removes element at index 4         
print(c)


# Slicing of an array
d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
e = arr.array('i', d)
print("d[1:5]: ", d[3:8])
print("d[:-2]: ", d[:-2])
print("d[:]: ", d[:])


# Searching Element in an array
print(a.index(33))
print(a.index(88))
