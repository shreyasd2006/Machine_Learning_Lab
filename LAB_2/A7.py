import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
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
sample = df.iloc[:20]
binary_cols = [c for c in sample.columns if sample[c].nunique() == 2]
jc = np.zeros((20, 20))
smc = np.zeros((20, 20))
cos = cosine_similarity(sample)
for i in range(20):
    for j in range(20):
        a = sample.iloc[i][binary_cols].to_numpy()
        b = sample.iloc[j][binary_cols].to_numpy()
        f11 = np.sum((a == 1) & (b == 1))
        f00 = np.sum((a == 0) & (b == 0))
        f10 = np.sum((a == 1) & (b == 0))
        f01 = np.sum((a == 0) & (b == 1))
        if f11 + f10 + f01 == 0:
            jc[i][j] = 1
        else:
            jc[i][j] = f11 / (f11 + f10 + f01)
        smc[i][j] = (f11 + f00) / (f11 + f00 + f10 + f01)
sns.heatmap(jc, annot=True)
plt.show()
sns.heatmap(smc, annot=True)
plt.show()
sns.heatmap(cos, annot=True)
plt.show()