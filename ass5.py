"""
ASSIGNMENT 5 - Logistic Regression

Problem Statement:
Perform classification using Logistic Regression
and generate confusion matrix.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score,recall_score
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Social_Network_Ads.csv")

# Features and target
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

cm = confusion_matrix(y_test, pred)
# Evaluation
print("Confusion Matrix:", cm)

# TN, FP, FN, TP = cm.ravel()

print("\nAccuracy:")
print(accuracy_score(y_test, pred))
print(precision_score(y_test,pred))
print(recall_score(y_test, pred))
error = accuracy_score(y_test, pred)- 1
print(error)

# print("Error Rate:", (FP + FN) / (TP + TN + FP + FN))
# print("Precision:", TP / (TP + FP))
# print("Recall:", TP / (TP + FN))    

# Heatmap of confusion matrix
sns.heatmap(cm, annot=True, fmt='d')
plt.show()