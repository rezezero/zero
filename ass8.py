"""
ASSIGNMENT 8 - Data Visualization I

Problem Statement:
Plot histogram for Titanic fare distribution.
"""

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')

# Histogram
plt.hist(df['fare'])

plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")

plt.show()