import numpy as np
import time
import numba

# Exercise 5: Optimize Performance Using Vectorization and Numba

# Part a: Vectorization

# Function to compute the element-wise square of an array using a for loop
def square_with_loop(arr):
    result = np.zeros_like(arr)
    for i in range(len(arr)):
        result[i] = arr[i] ** 2
    return result

# Function to compute the element-wise square of an array using NumPy vectorization
def square_with_vectorization(arr):
    return arr ** 2

# Create a large array of size 1,000,000 with random values
large_array = np.random.rand(1000000)

# Compare the performance of the two functions
start_time_loop = time.time()
square_with_loop(large_array)
end_time_loop = time.time()

start_time_vectorization = time.time()
square_with_vectorization(large_array)
end_time_vectorization = time.time()

print("Time taken with for loop:", end_time_loop - start_time_loop, "seconds")
print("Time taken with NumPy vectorization:", end_time_vectorization - start_time_vectorization, "seconds")

# Part b: Numba

# Use the @numba.jit decorator to optimize the function that uses a for loop

def square_with_numba(arr):
    result = np.zeros_like(arr)
    for i in range(len(arr)):
        result[i] = arr[i] ** 2
    return result

# Compare the performance of the Numba-optimized function with the vectorized NumPy function
start_time_numba = time.time()
square_with_numba(large_array)
end_time_numba = time.time()

print("Time taken with Numba optimization:", end_time_numba - start_time_numba, "seconds")
