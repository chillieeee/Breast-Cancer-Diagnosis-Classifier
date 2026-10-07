from sklearn.datasets import load_breast_cancer
import pandas as pd

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Grab one malignant (0) and one benign (1) example
malignant_sample = df[df['target'] == 0].iloc[0]
benign_sample = df[df['target'] == 1].iloc[0]

print("MALIGNANT SAMPLE:")
print(malignant_sample.drop('target').to_dict())

print("\nBENIGN SAMPLE:")
print(benign_sample.drop('target').to_dict())