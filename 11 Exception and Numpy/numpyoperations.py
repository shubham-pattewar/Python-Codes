import numpy as np

arr = np.arange(1,13)
print("Original array: ", arr)

# reshaping array 
shaped = arr.reshape(3,4)
print("Reshaped: \n", shaped)

# transpose
transposed = shaped.T
print("Transposed: \n", transposed)


# Arithmetic Operations
arr1 = np.array([10,20,30,40,50,60])
arr2 = np.array([1,2,3,4,5,6])

print("Array1: ", arr1)
print("Array2: ", arr2)
print("Addition: ", arr1 +arr2)
print("Substraction: ", arr1 - arr2)
print("Multiplication: ", arr1 * arr2)
print("Division: ", arr1 / arr2)
print("Division: ", arr1 // arr2)
