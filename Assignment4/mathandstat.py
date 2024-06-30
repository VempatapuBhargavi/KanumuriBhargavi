import numpy as np

# Exercise 3: Use NumPy for Mathematical and Statistical Calculations

# Part a: Mathematical functions
# Create an array of 10 evenly spaced values between 0 and 2π
values = np.linspace(0, 2 * np.pi, 10)

# Compute the sine, cosine, and tangent of each value
sine_values = np.sin(values)
cosine_values = np.cos(values)
tangent_values = np.tan(values)

# Print the results
print("Values:\n", values)
print("Sine values:\n", sine_values)
print("Cosine values:\n", cosine_values)
print("Tangent values:\n", tangent_values)

# Part b: Statistical functions
# Create a 3x3 array with random integers between 1 and 100
random_array = np.random.randint(1, 101, (3, 3))

# Compute the mean, median, standard deviation, and variance
mean_value = np.mean(random_array)
median_value = np.median(random_array)
std_deviation = np.std(random_array)
variance_value = np.var(random_array)

# Print the results
print("Random 3x3 array:\n", random_array)
print("Mean value:", mean_value)
print("Median value:", median_value)
print("Standard deviation:", std_deviation)
print("Variance:", variance_value)

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