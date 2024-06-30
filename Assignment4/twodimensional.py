import numpy as np

# Part a: Array arithmetic
# Create two 1-dimensional arrays of integers from 1 to 5 and 6 to 10
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

# Perform element-wise addition, subtraction, multiplication, and division
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

# Print the results
print("Addition:\n", addition)
print("Subtraction:\n", subtraction)
print("Multiplication:\n", multiplication)
print("Division:\n", division)

# Part b: Indexing and slicing
# Create a 5x5 array with values from 1 to 25
array_5x5 = np.arange(1, 26).reshape(5, 5)

# Extract the subarray consisting of the first two rows and columns
subarray = array_5x5[:2, :2]

# Print the extracted subarray
print("Subarray (first two rows and columns):\n", subarray)

# Part c: Boolean indexing
# Create a 1-dimensional array of integers from 10 to 19
array_10_to_19 = np.arange(10, 20)

# Extract elements greater than 15
greater_than_15 = array_10_to_19[array_10_to_19 > 15]

# Print the resulting array
print("Elements greater than 15:\n", greater_than_15)