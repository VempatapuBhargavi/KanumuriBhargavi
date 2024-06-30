import pandas as pd

# Sample Iris data
data = {
    'SepalLength': [5.1, 4.9, 4.7, 4.6, 5.0],
    'SepalWidth': [3.5, 3.0, 3.2, 3.1, 3.6],
    'PetalLength': [1.4, 1.4, 1.3, 1.5, 1.4],
    'PetalWidth': [0.2, 0.2, 0.2, 0.2, 0.2],
    'Species': ['setosa', 'setosa', 'setosa', 'setosa', 'setosa']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('iris.csv', index=False)
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the Iris dataset from a CSV file
df = pd.read_csv('iris.csv')

# Perform one-hot encoding on the Species column
df_onehot = pd.get_dummies(df, columns=['Species'], prefix='Species')

# Perform label encoding on the Species column
label_encoder = LabelEncoder()
df['Species_Label'] = label_encoder.fit_transform(df['Species'])

# Create a new feature PetalArea by multiplying PetalLength and PetalWidth
df['PetalArea'] = df['PetalLength'] * df['PetalWidth']

# Create a new feature SepalArea by multiplying SepalLength and SepalWidth
df['SepalArea'] = df['SepalLength'] * df['SepalWidth']

# Display the DataFrame with new features and encoded columns
print("DataFrame with One-Hot Encoding:")
print(df_onehot)

print("\nDataFrame with Label Encoding and New Features:")
print(df)