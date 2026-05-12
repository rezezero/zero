"""
ASSIGNMENT 6 - Naive Bayes

Problem Statement:
Perform classification using Naive Bayes algorithm.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

df = pd.read_csv("Iris.csv")

# Features and target
X = df.iloc[:, 1:5]
y = df['Species']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Create model
model = GaussianNB()

# Train model
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Evaluation
print("Confusion Matrix:")
print(confusion_matrix(y_test, pred))

print("\nAccuracy:")
print(accuracy_score(y_test, pred))