import pandas as pd
import numpy as np
from scipy.spatial.distance import minkowski
df = pd.read_excel("test.xlsx", sheet_name="marketing_campaign")
num = df.select_dtypes(include=np.number)
v1 = num.iloc[0]
v2 = num.iloc[1]
def my_minkowski(a, b, p):
    return np.sum(np.abs(a - b) ** p) ** (1 / p)
print("Own Function:", my_minkowski(v1, v2, 2))
print("Scipy Function:", minkowski(v1, v2, 2))