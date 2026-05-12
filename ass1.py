import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('Placement_data_full_class.csv')  

# Display first rows
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

#TO check if the data is missing
print(df.isna())
print(df.isna().sum())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Statistical summary
print("\nStatistics:")
print(df.describe())

#types of variable used
print("variables description")
print(df.dtypes)

#Dimension of dataframes
print("Check Data Frame Dimensions")
print(df.shape)

# Convert categorical column into numeric
# Example: Male=0, Female=1
if 'gender' in df.columns:
    df['gender'] = df['gender'].map({'M':0,'F':1})
    

print("\nUpdated Dataset:")
print(df.head())
