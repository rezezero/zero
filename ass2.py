"""
ASSIGNMENT 2 - Data Wrangling II
1. Handle missing values
2. Detect & handle outliers
3. Apply data transformation
"""

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("Placement_data_full_class.csv")

# Handle missing values
print("Missing Values:\n", df.isnull().sum())
df.fillna(df.mean(numeric_only=True), inplace=True)

# Select numeric columns
num_df = df.select_dtypes(include=np.number)

# Detect & handle outliers using IQR
Q1 = num_df.quantile(0.25)
Q3 = num_df.quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = ((num_df < lower) | (num_df > upper))
print("\nOutliers:\n", outliers)

# Capping outliers
df[num_df.columns] = num_df.clip(lower, upper, axis=1)

# Log transformation
if 'Salary' in df.columns:
    df['Salary'] = np.log(df['Salary'] + 1)

# Final dataset
print("\nUpdated Dataset:\n", df.head())