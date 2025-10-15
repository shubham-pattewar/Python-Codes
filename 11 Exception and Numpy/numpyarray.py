import numpy as np

# 1 dimentional array
arr1 = np.array([1, 2, 3, "Hello", "#", 4, 5, "why"])
print(arr1)


# 2 dimentional array
arr2 = np.array([[1,2,3,4], [2,3,3,4]])

print("Exact Array: ")
print(arr2)

print("Elements in 2D array: ")
print(arr2[1])
print(arr2[1][2])
print(arr2[0])


# 3 dimentional array
arr3 = np.array([
    [[1,2,3,4], [5,6,7,8]], 
    [[2,5,6,7], [9,7,8,8]],
    [[7,8,6,8], [3,6,5,8]]
    ])
print(arr3)

print(arr3[1])
print(arr3[1][1])
print(arr3[0][1][3])
