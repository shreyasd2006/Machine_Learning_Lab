import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel("test.xlsx", sheet_name="marketing_campaign")
num = df.select_dtypes(include=np.number)
v1 = num.iloc[0]
v2 = num.iloc[1]
def minkowski_distance(a, b, p):
    return np.sum(np.abs(a - b) ** p) ** (1 / p)
dist = []
for p in range(1, 11):
    dist.append(minkowski_distance(v1, v2, p))
plt.plot(range(1, 11), dist, marker="o")
plt.xlabel("p")
plt.ylabel("Distance")
plt.title("Minkowski Distance")
plt.grid(True)
plt.show()