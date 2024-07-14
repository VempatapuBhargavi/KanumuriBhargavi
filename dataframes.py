import pandas as pd

# Sample data for demonstration purposes
data1 = {'id': [1, 2, 3], 'value1': ['A', 'B', 'C']}
data2 = {'id': [2, 3, 4], 'value2': ['X', 'Y', 'Z']}
data3 = {'id': [5, 6, 7], 'value1': ['D', 'E', 'F']}

# Load two DataFrames, df1 and df2, with a common column id
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# Perform an inner join on the id column
inner_join_df = pd.merge(df1, df2, on='id', how='inner')
print("Inner Join DataFrame:")
print(inner_join_df)

# Perform an outer join on the id column
outer_join_df = pd.merge(df1, df2, on='id', how='outer')
print("\nOuter Join DataFrame:")
print(outer_join_df)

# Load two DataFrames with the same columns
df4 = df1.copy()
df5 = df3.copy()

# Concatenate the DataFrames vertically
concatenated_df = pd.concat([df4, df5], ignore_index=True)
print("\nConcatenated DataFrame:")
print(concatenated_df)