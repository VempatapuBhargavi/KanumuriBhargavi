import numpy as np
from scipy import stats

# Set the random seed for reproducibility
np.random.seed(42)

# Generate a sample dataset of 30 random values from a normal distribution with mean 60 and std dev 10
sample_data = np.random.normal(loc=60, scale=10, size=30)

# Known population mean to test against
population_mean = 50

# Perform a one-sample t-test
t_statistic, p_value = stats.ttest_1samp(sample_data, population_mean)

# Output the results
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")

# Interpretation
if p_value < 0.05:
    print("The sample mean is significantly different from the population mean of 50.")
else:
    print("The sample mean is not significantly different from the population mean of 50.")