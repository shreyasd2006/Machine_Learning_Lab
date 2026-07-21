import pandas as pd
import numpy as np
df = pd.read_excel("test.xlsx", sheet_name="thyroid0387_UCI")
binary = []
for c in df.columns:
    values = set(df[c].dropna().astype(str).unique())
    if len(values) <= 2:
        binary.append(c)
v1 = df.loc[0, binary].astype(str)
v2 = df.loc[1, binary].astype(str)
f11 = np.sum((v1 == "t") & (v2 == "t"))
f00 = np.sum((v1 != "t") & (v2 != "t"))
f10 = np.sum((v1 == "t") & (v2 != "t"))
f01 = np.sum((v1 != "t") & (v2 == "t"))
jc = f11 / (f11 + f10 + f01)
smc = (f11 + f00) / (f11 + f10 + f01 + f00)
print(jc)
print(smc)