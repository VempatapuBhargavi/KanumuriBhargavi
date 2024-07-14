import pandas as pd
import matplotlib.pyplot as plt

# Sample time series data for demonstration purposes
data = {
    'date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'value': [10, 15, 14, 18, 16, 20, 21, 19, 22, 25]
}

# Load the time series dataset into a DataFrame
df = pd.DataFrame(data)

# Ensure the 'date' column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Set the 'date' column as the index of the DataFrame
df.set_index('date', inplace=True)

# Create a line plot to visualize the trend over time
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['value'], marker='o')
plt.title('Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()