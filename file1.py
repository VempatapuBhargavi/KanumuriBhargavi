import pandas as pd
import numpy as np

# 1. Load a dataset with missing values
df_missing = pd.read_csv('missing_values.csv')

# Identify the columns with missing values
missing_columns = df_missing.columns[df_missing.isnull().any()].tolist()
print("Columns with missing values:", missing_columns)

# Fill the missing values with the mean of the column
df_missing_filled = df_missing.fillna(df_missing.mean())
print("\nDataFrame after filling missing values with mean:\n", df_missing_filled)

# 2. Load a dataset where numerical columns are mistakenly read as strings
df_strings = pd.read_csv('numerical_as_strings.csv')

# Convert the columns to appropriate data types
for col in df_strings.columns:
    if df_strings[col].dtype == 'object':
        try:
            df_strings[col] = pd.to_numeric(df_strings[col])
        except ValueError:
            pass

print("\nDataFrame after converting numerical columns from strings to appropriate data types:\n", df_strings)

# 3. Load a dataset with duplicate rows
df_duplicates = pd.read_csv('duplicates.csv')

# Remove the duplicate rows
df_no_duplicates = df_duplicates.drop_duplicates()

print("\nDataFrame after removing duplicate rows:\n", df_no_duplicates)
