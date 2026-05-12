import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Iris.csv")

# Display first 5 rows
print(df.head())

# Information about dataset
print(df.info())

# Statistical summary
print(df.describe())

# Check null values
print(df.isnull().sum())

# Feature types
print(df.dtypes)

# Histograms
sns.histplot(df['SepalLengthCm'], kde=True)
plt.show()

sns.histplot(df['SepalWidthCm'], kde=True)
plt.show()

sns.histplot(df['PetalLengthCm'], kde=True)
plt.show()

sns.histplot(df['PetalWidthCm'], kde=True)
plt.show()

# Boxplots
sns.boxplot(x=df['SepalLengthCm'])
plt.show()

sns.boxplot(x=df['SepalWidthCm'])
plt.show()

sns.boxplot(x=df['PetalLengthCm'])
plt.show()

sns.boxplot(x=df['PetalWidthCm'])
plt.show()