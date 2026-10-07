import pandas as pd
from sklearn.datasets import load_breast_cancer

# Load the dataset
data = load_breast_cancer()

# Convert to a DataFrame for easier viewing
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target  # 0 = malignant, 1 = benign

# Basic info
print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nTarget value counts:")
print(df['target'].value_counts())
print("\n(0 = malignant, 1 = benign)")

print("\nAny missing values?")
print(df.isnull().sum().sum())