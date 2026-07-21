import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
df = pd.read_excel("test.xlsx", sheet_name="thyroid0387_UCI")
for c in df.columns:
    df[c] = df[c].replace("?", pd.NA)
    try:
        df[c] = pd.to_numeric(df[c])
        df[c] = df[c].fillna(df[c].median())
    except:
        df[c] = df[c].fillna(df[c].mode()[0])
        df[c] = LabelEncoder().fit_transform(df[c].astype(str))
numeric = df.select_dtypes(include="number").columns
scaler = MinMaxScaler()
df[numeric] = scaler.fit_transform(df[numeric])
print(df.head())