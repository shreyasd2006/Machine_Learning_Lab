import pandas as pd
from sklearn.preprocessing import LabelEncoder
df = pd.read_excel("test.xlsx", sheet_name="thyroid0387_UCI")
for c in df.columns:
    df[c] = df[c].replace("?", pd.NA)
    try:
        df[c] = pd.to_numeric(df[c])
        q1 = df[c].quantile(0.25)
        q3 = df[c].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        if ((df[c] < lower) | (df[c] > upper)).any():
            df[c] = df[c].fillna(df[c].median())
        else:
            df[c] = df[c].fillna(df[c].mean())
    except:
        df[c] = df[c].fillna(df[c].mode()[0])
        df[c] = LabelEncoder().fit_transform(df[c].astype(str))
print(df.head())