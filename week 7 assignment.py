import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# Use a non-interactive backend
matplotlib.use('Agg')

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', np.nan, 'Diana', 'Eve', 'Frank', np.nan, 'Hank', 'Ivy', 'John'],
    'Age': [25, np.nan, 35, 29, 32, 40, 31, 28, 30, 31],
    'Salary': [50000, 60000, 55000, np.nan, 58000, np.nan, 52000, 61000, 59000, 56000],
    'Department': ['HR', 'IT', 'Finance', 'IT', np.nan, 'HR', 'Finance', 'IT', 'HR', np.nan]
}

df = pd.DataFrame(data)

# Display the original dataset
print("Original Dataset:")
print(df)

# Dataset info
print("\nDataset Info:")
print(df.info())

# Missing values per column
print("\nMissing Values per Column:")
print(df.isnull().sum())

# Fill missing values (impute with mean for numeric columns, 'Unknown' for categorical columns)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Department'].fillna('Unknown', inplace=True)
df['Name'].fillna('Unknown', inplace=True)

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df)

# Missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Basic statistics of numerical columns
print("\nBasic Statistics of Numerical Columns:")
print(df[['Age', 'Salary']].describe())

# Average salary by department
print("\nAverage Salary by Department:")
print(df.groupby('Department')['Salary'].mean())

# Plot salary distribution by department
plt.figure(figsize=(10, 6))
sns.barplot(x='Department', y='Salary', data=df, hue='Department', palette='viridis')
plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')

# Save the plot to a file
plt.savefig('barplot.png')

# Plot age distribution by department
plt.figure(figsize=(10, 6))
sns.boxplot(x='Department', y='Age', data=df, palette='viridis')
plt.title('Age Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Age')

# Save the plot to a file
plt.savefig('boxplot.png')

# Plot salary distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Salary'], kde=True, color='blue')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')

# Save the plot to a file
plt.savefig('salary_distribution.png')

# Show the plots (not necessary since we are saving them, but can be included if interactive backend is set up)
# plt.show()  # You can remove this line if you're using a non-interactive backend
