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

except Exception as e:
    print(f"Error loading dataset: {e}")

# Task 2: Basic Data Analysis
print("\nBasic statistics:")
print(df.describe())

# Grouping by species and calculating mean values
species_group = df.groupby('species', as_index=False).mean()
print("\nMean values for each species:")
print(species_group)

# Task 3: Data Visualization
sns.set(style="whitegrid")

# Line Chart: Sepal Length trend (ordered by species)
plt.figure(figsize=(10, 5))
df_sorted = df.sort_values(by=['species', 'sepal length (cm)'])
plt.plot(df_sorted.index, df_sorted['sepal length (cm)'], label='Sepal Length', linestyle='-', marker='o', color='blue')
plt.xlabel('Index (Sorted)')
plt.ylabel('Sepal Length (cm)')
plt.title('Trend of Sepal Length Over Index')
plt.legend()
plt.show()

# Bar Chart: Average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal length (cm)', data=df, palette='viridis', estimator=np.mean)
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
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep', s=100)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Sepal Length vs. Petal Length by Species')
plt.legend(title='Species')
plt.show()
