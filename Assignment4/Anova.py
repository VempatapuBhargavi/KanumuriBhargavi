import numpy as np
from scipy.stats import f_oneway

# Set the random seed for reproducibility
np.random.seed(0)

# Generate sample datasets
group1 = np.random.normal(50, 10, 20)
group2 = np.random.normal(55, 10, 20)
group3 = np.random.normal(60, 10, 20)

# Perform one-way ANOVA
f_statistic, p_value = f_oneway(group1, group2, group3)

# Output results
print(f"F-statistic: {f_statistic}")
print(f"p-value: {p_value}")