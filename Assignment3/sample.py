import numpy as np
from scipy.stats import ttest_ind

# Generate sample data
np.random.seed(42)
sample1 = np.random.normal(loc=55, scale=8, size=25)
sample2 = np.random.normal(loc=60, scale=8, size=25)

# Perform the two-sample t-test
t_stat, p_value = ttest_ind(sample1, sample2)

# Print the results
print("T-value:", t_stat)
print("P-Value:", p_value)

# Interpret the results
alpha = 0.05
if p_value > alpha:
    print("No evidence to reject the null hypothesis that the means are equal.")
else:
    print("There is significant evidence to reject the null hypothesis that the means are equal.")