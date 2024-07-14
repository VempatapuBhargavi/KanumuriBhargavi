import numpy as np
from scipy.stats import chi2_contingency

# Observed frequencies
observed = np.array([[10, 15],
                     [20, 25]])

# Perform Chi-Squared test
chi2, p, dof, expected = chi2_contingency(observed)

# Output results
print(f"Chi-Squared statistic: {chi2}")
print(f"p-value: {p}")
print(f"Degrees of Freedom: {dof}")
print(f"Expected frequencies: \n{expected}")