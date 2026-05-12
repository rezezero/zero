"""
ASSIGNMENT 9 - Data Visualization II

Problem Statement:
Plot boxplot for age distribution with gender and survival.
"""

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic_data.csv')

# Boxplot
sns.boxplot(
    x='sex',
    y='age',
    hue='survived',
    data=df
)

plt.title("Age Distribution")

plt.show()