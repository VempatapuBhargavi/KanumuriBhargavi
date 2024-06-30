import pandas as pd

# Load the CSV file into a Pandas DataFrame
csv_df = pd.read_csv('data.csv')

# Load the JSON file into a Pandas DataFrame
json_df = pd.read_json('data.json')

# Load the Excel file into a Pandas DataFrame
excel_df = pd.read_excel('data.xlsx')

# Function to ask the user how many rows to display and then display the rows
def display_rows(df):
    try:
        n = int(input("How many rows would you like to display? "))
        print(df.head(n))
    except ValueError:
        print("Please enter a valid number.")

# Display rows for each DataFrame
print("CSV DataFrame:")
display_rows(csv_df)

print("\nJSON DataFrame:")
display_rows(json_df)

print("\nExcel DataFrame:")
display_rows(excel_df)