import pandas as pd

# Sample data for demonstration purposes
data1 = {'category': ['A', 'B', 'A', 'B', 'C', 'A'], 'value': [10, 20, 30, 40, 50, 60]}
data2 = {'category': ['A', 'B', 'A', 'B', 'C', 'A'], 'value': [10, 20, 30, 40, 50, 60]}
data3 = {'category': ['A', 'A', 'B', 'B', 'C', 'C'], 'subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'], 'value': [5, 10, 15, 20, 25, 30]}

# Load a dataset with columns category and value
df1 = pd.DataFrame(data1)

# Group the data by category and compute the sum of value for each category
sum_df = df1.groupby('category')['value'].sum().reset_index()
print("Sum of value for each category:")
print(sum_df)

# Load another dataset with columns category and value
df2 = pd.DataFrame(data2)

# Group the data by category and compute the mean and standard deviation of value for each category
mean_std_df = df2.groupby('category')['value'].agg(['mean', 'std']).reset_index()
print("\nMean and standard deviation of value for each category:")
print(mean_std_df)

# Load a dataset with columns category, subcategory, and value
df3 = pd.DataFrame(data3)

# Create a pivot table that shows the sum of value for each combination of category and subcategory
pivot_table = pd.pivot_table(df3, values='value', index='category', columns='subcategory', aggfunc='sum').reset_index()
print("\nPivot table showing sum of value for each combination of category and subcategory:")
print(pivot_table)