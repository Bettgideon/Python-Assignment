import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
    
    print("\nFirst few rows of the dataset:")
    print(df.head())
    
    print("\nDataset Info:")
    print(df.info())
    
    print("\nChecking for missing values:")
    print(df.isnull().sum())
    
    # No missing values in this dataset, but if there were, we could fill/drop them:
    # df.fillna(method='ffill', inplace=True)
except Exception as e:
    print(f"Error loading dataset: {e}")

# Task 2: Basic Data Analysis
print("\nBasic statistics:")
print(df.describe())

# Grouping by species and calculating mean values
species_group = df.groupby('species').mean()
print("\nMean values for each species:")
print(species_group)

# Task 3: Data Visualization
sns.set(style="whitegrid")

# Line Chart: Trend over index (since no time variable, using index as x-axis)
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length', linestyle='-', marker='o')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.title('Trend of Sepal Length Over Index')
plt.legend()
plt.show()

# Bar Chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal length (cm)', data=df, palette='viridis')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.title('Average Petal Length per Species')
plt.show()

# Histogram: Distribution of Sepal Width
plt.figure(figsize=(8, 5))
sns.histplot(df['sepal width (cm)'], bins=20, kde=True, color='blue')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Width')
plt.show()

# Scatter Plot: Sepal Length vs. Petal Length
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Sepal Length vs. Petal Length by Species')
plt.legend(title='Species')
plt.show()
