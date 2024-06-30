import numpy as np
from scipy import stats

# Set the random seed for reproducibility
np.random.seed(42)

# Generate a sample dataset of 30 random values from a normal distribution with mean 50 and standard deviation 5
sample_data = np.random.normal(50, 5, 30)

# Perform a one-sample t-test to check if the sample mean is significantly different from 50
t_statistic, p_value = stats.ttest_1samp(sample_data, 50)

# Define the significance level (alpha)
alpha = 0.05

# Check if the p-value is less than alpha to determine significance
if p_value < alpha:
    print("The sample mean is significantly different from 50 (reject the null hypothesis)")
else:
    print("The sample mean is not significantly different from 50 (fail to reject the null hypothesis)")

# Display the t-statistic and p-value
print("t-statistic:", t_statistic)
print("p-value:", p_value)