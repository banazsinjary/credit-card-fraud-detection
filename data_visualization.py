
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Class Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Class', data=df, palette=['blue', 'red'])
plt.title("Class Distribution: Fraud vs. Non-Fraud")
plt.xlabel("Class (0 = Non-Fraud, 1 = Fraud)")
plt.ylabel("Count")
plt.xticks(ticks=[0, 1], labels=["Non-Fraud", "Fraud"])
plt.show()

# Transaction Amounts Summary
plt.figure(figsize=(8,5))
sns.boxplot(x='Class', y='Amount', data=df, hue='Class', legend=False, palette={0: 'blue', 1: 'red'})
plt.ylim(0, df['Amount'].quantile(0.95))  # Adjusting outliers
plt.title("Transaction Amount Distribution by Class")
plt.xlabel("Class (0 = Non-Fraud, 1 = Fraud)")
plt.ylabel("Transaction Amount")
plt.show()

# Fraud Time 
plt.figure(figsize=(10,5))
sns.histplot(df[df['Class'] == 0]['Time'], bins=50, color='blue', label="Non-Fraud", kde=True)
sns.histplot(df[df['Class'] == 1]['Time'], bins=50, color='red', label="Fraud", kde=True)
plt.title("Fraud Time Analysis")
plt.xlabel("Time (Seconds from First Transaction)")
plt.ylabel("Frequency")
plt.legend()
plt.show()
