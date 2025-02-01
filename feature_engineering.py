
import pandas as pd

df = pd.read_csv('creditcard_cleaned.csv')


print("Class Distribution:")
class_distribution = df['Class'].value_counts()
print(class_distribution)

print("\nTransaction Amounts Summary:")
amount_stats = df.groupby('Class')['Amount'].describe()
print(amount_stats)


print("\nFraud Time Analysis:")
fraud_time_analysis = df.groupby('Class')['Time'].describe()
print(fraud_time_analysis)

