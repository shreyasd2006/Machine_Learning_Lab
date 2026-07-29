import pandas as pd
import numpy as np
df = pd.read_excel("test.xlsx", sheet_name="marketing_campaign")
num = df.select_dtypes(include=np.number)
A = num.iloc[0].values
B = num.iloc[1].values
def dot_product(a, b):
    s = 0
    for i in range(len(a)):
        s += a[i] * b[i]
    return s
def vector_length(a):
    s = 0
    for i in a:
        s += i * i
    return s ** 0.5
print("Own Dot:", dot_product(A, B))
print("NumPy Dot:", np.dot(A, B))
print("Own Norm A:", vector_length(A))
print("NumPy Norm A:", np.linalg.norm(A))
print("Own Norm B:", vector_length(B))
print("NumPy Norm B:", np.linalg.norm(B))