import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import matplotlib.pyplot as plt

# Load the Titanic dataset from a CSV file
df = pd.read_csv('titanic.csv')

# Identify and handle missing values in the Age, Embarked, and Cabin columns using different imputation methods

# Impute Age with the median
age_imputer = SimpleImputer(strategy='median')
df['Age'] = age_imputer.fit_transform(df[['Age']])

# Impute Embarked with the most frequent value
embarked_imputer = SimpleImputer(strategy='most_frequent')
df['Embarked'] = embarked_imputer.fit_transform(df[['Embarked']])

# Impute Cabin with a placeholder for missing values
df['Cabin'] = df['Cabin'].fillna('Unknown')

# Standardize the numerical features (Age, Fare) using StandardScaler
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Normalize the numerical features using MinMaxScaler
minmax_scaler = MinMaxScaler()
df[['Age_norm', 'Fare_norm']] = minmax_scaler.fit_transform(df[['Age', 'Fare']])

# Compare the distributions of the scaled features using histograms
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Age before and after standardization
axes[0, 0].hist(df['Age'], bins=20, color='blue', alpha=0.7, label='Standardized Age')
axes[0, 0].set_title('Standardized Age')
axes[0, 0].legend()

# Fare before and after standardization
axes[0, 1].hist(df['Fare'], bins=20, color='green', alpha=0.7, label='Standardized Fare')
axes[0, 1].set_title('Standardized Fare')
axes[0, 1].legend()

# Age after normalization
axes[1, 0].hist(df['Age_norm'], bins=20, color='orange', alpha=0.7, label='Normalized Age')
axes[1, 0].set_title('Normalized Age')
axes[1, 0].legend()

# Fare after normalization
axes[1, 1].hist(df['Fare_norm'], bins=20, color='red', alpha=0.7, label='Normalized Fare')
axes[1, 1].set_title('Normalized Fare')
axes[1, 1].legend()

plt.tight_layout()
plt.show()
age_imputer = SimpleImputer(strategy='median')
df['Age'] = age_imputer.fit_transform(df[['Age']])
embarked_imputer = SimpleImputer(strategy='most_frequent')
df['Embarked'] = embarked_imputer.fit_transform(df[['Embarked']])
df['Cabin'] = df['Cabin'].fillna('Unknown')
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
minmax_scaler = MinMaxScaler()
df[['Age_norm', 'Fare_norm']] = minmax_scaler.fit_transform(df[['Age', 'Fare']])
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].hist(df['Age'], bins=20, color='blue', alpha=0.7, label='Standardized Age')
axes[0, 0].set_title('Standardized Age')
axes[0, 0].legend()

axes[0, 1].hist(df['Fare'], bins=20, color='green', alpha=0.7, label='Standardized Fare')
axes[0, 1].set_title('Standardized Fare')
axes[0, 1].legend()

axes[1, 0].hist(df['Age_norm'], bins=20, color='orange', alpha=0.7, label='Normalized Age')
axes[1, 0].set_title('Normalized Age')
axes[1, 0].legend()

axes[1, 1].hist(df['Fare_norm'], bins=20, color='red', alpha=0.7, label='Normalized Fare')
axes[1, 1].set_title('Normalized Fare')
axes[1, 1].legend()

plt.tight_layout()
plt.show()