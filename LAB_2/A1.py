import pandas as pd
import numpy as np
df = pd.read_excel("test.xlsx", sheet_name="Purchase data")
X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]].to_numpy()
y = df["Payment (Rs)"].to_numpy().reshape(-1, 1)
print("Dimensionality:", X.shape[1])
print("Number of vectors:", X.shape[0])
print("Rank:", np.linalg.matrix_rank(X))
cost = np.linalg.pinv(X) @ y
print(cost)