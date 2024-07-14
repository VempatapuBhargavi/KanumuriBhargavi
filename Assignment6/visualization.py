import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset from a CSV file
df = pd.read_csv('titanic.csv')

# Create box plots to identify outliers in the Age and Fare columns
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.boxplot(data=df, x='Age')
plt.title('Box Plot of Age')

plt.subplot(1, 2, 2)
sns.boxplot(data=df, x='Fare')
plt.title('Box Plot of Fare')

plt.show()

# Create histograms and KDE plots to visualize the distribution of Age and Fare
plt.figure(figsize=(14, 6))

plt.subplot(2, 2, 1)
sns.histplot(df['Age'].dropna(), kde=True)
plt.title('Histogram and KDE of Age')

plt.subplot(2, 2, 2)
sns.histplot(df['Fare'], kde=True)
plt.title('Histogram and KDE of Fare')

plt.show()

# Create scatter plots to visualize the relationship between Age and Fare, and Pclass and Survived
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='Age', y='Fare')
plt.title('Scatter Plot of Age vs Fare')

plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='Pclass', y='Survived', alpha=0.6)
plt.title('Scatter Plot of Pclass vs Survived')

plt.show()

# Use pair plots to visualize the relationships between multiple numerical features
numerical_features = ['Age', 'Fare', 'SibSp', 'Parch']
sns.pairplot(df[numerical_features].dropna())
plt.show()