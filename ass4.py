"""
ASSIGNMENT 4 - Linear Regression

Problem Statement:
Predict house prices using Linear Regression.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("BostonHousing.csv")

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Fill missing values using median
df.fillna(df.median(numeric_only=True), inplace=True)

# Feature and target variable
X = df[['rm']]
y = df['medv']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict values
y_pred = model.predict(X_test)

# Print predictions
print("Predicted Values:")
print(y_pred)

# Plot graph
plt.scatter(y_test, y_pred)

plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")

plt.show()