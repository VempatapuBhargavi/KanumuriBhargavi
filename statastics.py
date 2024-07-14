import numpy as np
from scipy import stats

# Create a dataset with 20 random values between 1 and 100
np.random.seed(42)  # Set a seed for reproducibility
data = np.random.randint(1, 101, 20)

# Compute the mean, median, standard deviation, variance, skewness, and kurtosis
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
variance = np.var(data)
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

# Display the computed statistics
print("Dataset:", data)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Variance:", variance)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)