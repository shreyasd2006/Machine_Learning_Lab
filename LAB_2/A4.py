import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
df = pd.read_excel("test.xlsx", sheet_name="thyroid0387_UCI")
print(df.dtypes)
for c in df.columns:
    if df[c].dtype == object:
        print(c, df[c].unique()[:10])
print(df.describe())
print(df.isnull().sum())
for c in df.select_dtypes(include=np.number).columns:
    q1 = df[c].quantile(0.25)
    q3 = df[c].quantile(0.75)
    iqr = q3 - q1
    outliers = df[(df[c] < q1 - 1.5 * iqr) | (df[c] > q3 + 1.5 * iqr)]
    print(c, len(outliers))
for c in df.select_dtypes(include=np.number).columns:
    print(c, df[c].mean(), df[c].var())
label_df = df.copy()
for c in label_df.select_dtypes(include="object").columns:
    label_df[c] = LabelEncoder().fit_transform(label_df[c].astype(str))
onehot_df = pd.get_dummies(df)
print(label_df.head())
print(onehot_df.head())