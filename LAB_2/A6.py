import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_excel("test.xlsx", sheet_name="thyroid0387_UCI")
for c in df.columns:
    df[c] = df[c].astype(str).replace("?", pd.NA)
    df[c] = df[c].fillna(df[c].mode()[0])
    try:
        df[c] = pd.to_numeric(df[c])
    except:
        df[c] = LabelEncoder().fit_transform(df[c])
v1 = df.iloc[[0]]
v2 = df.iloc[[1]]
print(cosine_similarity(v1, v2))