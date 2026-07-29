import pandas as pd
df = pd.read_excel("test.xlsx", sheet_name="marketing_campaign")
categorical = df.select_dtypes(include="object").columns
label_df = df.copy()
for col in categorical:
    label_df[col] = label_df[col].astype("category").cat.codes
onehot_df = pd.get_dummies(df, columns=categorical)
print("Original Shape:", df.shape)
print("Label Encoded Shape:", label_df.shape)
print("One Hot Encoded Shape:", onehot_df.shape)