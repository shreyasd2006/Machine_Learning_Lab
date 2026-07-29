import pandas as pd
import numpy as np
df = pd.read_excel("test.xlsx", sheet_name="marketing_campaign")
num = df.select_dtypes(include=np.number)
def mean(x):
    return sum(x) / len(x)
def variance(x):
    m = mean(x)
    return sum((i - m) ** 2 for i in x) / len(x)
def std(x):
    return variance(x) ** 0.5
for col in num.columns:
    print(col)
    print("Mean:", mean(num[col]))
    print("Variance:", variance(num[col]))
    print("Std:", std(num[col]))
    print()