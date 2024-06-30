import numpy as np
import time

# Exercise 4: Implement Broadcasting and Vectorized Operations

# Part a: Broadcasting
# Create a 3x1 array with values from 1 to 3
array_3x1 = np.array([[1], [2], [3]])

# Create a 1x3 array with values from 4 to 6
array_1x3 = np.array([4, 5, 6])

# Add the two arrays using broadcasting
broadcasted_sum = array_3x1 + array_1x3

# Print the resulting array
print("3x1 array:\n", array_3x1)
print("1x3 array:\n", array_1x3)
print("Result of broadcasting addition:\n", broadcasted_sum)

# Part b: Vectorized operations
# Create two large arrays of size 1,000,000 with random values
array1_large = np.random.rand(1000000)
array2_large = np.random.rand(1000000)

# Compute the element-wise product of the two arrays
start_time = time.time()
elementwise_product = array1_large * array2_large
end_time = time.time()

# Print the time taken for the computation using vectorized operations
print("Time taken for element-wise product computation:", end_time - start_time, "seconds")