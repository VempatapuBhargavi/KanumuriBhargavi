import pandas as pd

# Load datasets
df_csv = pd.read_csv('data.csv')
df_json = pd.read_json('data.json')
df_excel = pd.read_excel('data.xlsx')

# Ask user for the number of rows to display
num_rows = int(input("How many rows would you like to display from each DataFrame? "))

# Display the specified number of rows from each DataFrame
print("\nCSV DataFrame:")
print(df_csv.head(num_rows))

print("\nJSON DataFrame:")
print(df_json.head(num_rows))

print("\nExcel DataFrame:")
print(df_excel.head(num_rows))