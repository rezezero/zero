import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------- PART A ----------------

df = pd.read_csv("Social_Network_Ads.csv")

# Basic Statistics
print(df.describe())

print("Mean =", df['EstimatedSalary'].mean())
print("Mode =", df['EstimatedSalary'].mode()[0])
print("Min =", df['EstimatedSalary'].min())
print("Max =", df['EstimatedSalary'].max())
print("Median =", df['EstimatedSalary'].median())
print("Std =", df['EstimatedSalary'].std())
print("Variance =", df['EstimatedSalary'].var())

# Grouped Statistics
print(df.groupby('Age')['EstimatedSalary']
      .agg(['min','max','mean','median','std','var']))


# ----- Plotting -----

# Bar Plot
sns.barplot(x='Gender', y='EstimatedSalary', data=df)
plt.title("Salary by Gender")
plt.show()

# Box Plot
sns.boxplot(x='Gender', y='EstimatedSalary', data=df)
plt.title("Boxplot of Salary")
plt.show()


# ---------------- PART B ----------------

df2 = pd.read_csv("iris.csv")

# Basic statistics
print(df2.describe())

# Species wise statistics
print(df2.groupby('Species').mean())
print(df2.groupby('Species').median())
print(df2.groupby('Species').max())
print(df2.groupby('Species').min())
print(df2.groupby('Species').std())
print(df2.groupby('Species').var())

# Mode of species
print("Mode =", df2['Species'].mode()[0])


# ----- Plotting -----

# Bar Plot
sns.barplot(x='Species', y='SepalLengthCm', data=df2)
plt.title("Sepal Length by Species")
plt.show()

# Box Plot
sns.boxplot(x='Species', y='SepalLengthCm', data=df2)
plt.title("Petal Length by Species")
plt.show()