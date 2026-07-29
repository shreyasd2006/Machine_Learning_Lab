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
my_mean = num.apply(mean)
my_std = num.apply(std)
np_mean = num.mean()
np_std = num.std(ddof=0)
print("Own Mean")
print(my_mean)
print("\nNumPy Mean")
print(np_mean)
print("\nOwn Std")
print(my_std)
print("\nNumPy Std")
print(np_std)