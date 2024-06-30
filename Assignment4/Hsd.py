import numpy as np
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Set the random seed for reproducibility
np.random.seed(0)

# Generate sample datasets
group1 = np.random.normal(50, 10, 20)
group2 = np.random.normal(55, 10, 20)
group3 = np.random.normal(60, 10, 20)

# Combine the data into a single array and create group labels
data = np.concatenate([group1, group2, group3])
groups = ['Group 1'] * 20 + ['Group 2'] * 20 + ['Group 3'] * 20

# Perform Tukey's HSD test
tukey_result = pairwise_tukeyhsd(data, groups)

# Output results
print(tukey_result)